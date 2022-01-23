#!/usr/bin/env python
import os
import sys
import json
import requests
from fontTools.subset import main
from pathlib import Path
from multiprocessing import Pool

CACHE_JSONS = {}
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PACKAGES_DIR = os.path.join(ROOT_DIR, "packages")
PACKAGES = [
    "lxgw-wenkai-webfont",
    "lxgw-wenkai-tc-webfont",
    "lxgw-wenkai-lite-webfont",
    "lxgw-wenkai-screen-webfont",
]
f = open('unicode.json', 'r')
UNICODE_RANGES = json.load(f)
f.close()

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def get_latest_release(repo):
    if repo == "lxgw-wenkai-webfont":
        repo = "LXGWWenKai"
    if repo == "lxgw-wenkai-tc-webfont":
        repo = "LXGWWenKaiTC"
    if repo == "lxgw-wenkai-lite-webfont":
        repo = "LXGWWenKai-Lite"
    if repo == "lxgw-wenkai-screen-webfont":
        repo = "LXGWWenKai-Screen"
    if CACHE_JSONS.get(repo):
        return CACHE_JSONS[repo]
    r = requests.get("https://api.github.com/repos/lxgw/{}/releases/latest"
        .format(repo))
    if r.status_code == 200:
        CACHE_JSONS[repo] = r.json()
        return r.json()
    return None

def package_dir(package):
    return os.path.join(PACKAGES_DIR, package)

def package_source_dir(package):
    return os.path.join(package_dir(package), "source")

def diff_version(package):
    version_file = os.path.join(package_dir(package), "VERSION")
    if not os.path.exists(version_file):
        current_version = "0"
    else:
        f = open(version_file, 'r')
        current_version = f.read().strip()
        f.close()
    latest_release = get_latest_release(package)
    latest_version = latest_release["tag_name"]
    should_update = True if current_version != latest_version else False
    return (should_update, latest_version)

def download_assets(package):
    source_dir = package_source_dir(package)
    ensure_dir(source_dir)
    release = get_latest_release(package)
    assets = filter(lambda a: a["name"].endswith(".ttf"), release["assets"])
    for asset in assets:
        name = asset["name"]
        url = asset["browser_download_url"]
        print("Downloading {}".format(name))
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(os.path.join(source_dir, name.lower()), 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
        else:
            print("Error downloading {}: {}".format(url, r.status_code))
            sys.exit(1)

def build_npm_package(package):
    source_dir = package_source_dir(package)
    files_dir = os.path.join(package_dir(package), "files")
    ensure_dir(files_dir)
    fonts = filter(lambda f: f.endswith(".ttf"), os.listdir(source_dir))
    tasks = []
    main_css = ""
    for font in fonts:
        font_weight = 400
        if "bold" in font:
            font_weight = 700
        elif "light" in font:
            font_weight = 300
        # lxgw-wenkai
        font_family = "LXGW WenKai"
        if "mono" in font:
            font_family = "LXGW WenKai Mono"
        # lxgw-wenkai-tc
        if "tc" in font:
            font_family = "LXGW WenKai TC"
        if "monotc" in font:
            font_family = "LXGW WenKai Mono TC"
        # lxgw-wenkai-lite
        if "lite" in font:
            font_family = "LXGW WenKai Lite"
        if "monolite" in font:
            font_family = "LXGW WenKai Mono Lite"
        # lxgw-wenkai-screen
        if "screen" in font:
            font_family = "LXGW WenKai Screen"
        if "screenr" in font:
            font_family = "LXGW WenKai Screen R"

        css = ""
        for part,unicode in UNICODE_RANGES.items():
            subset_id = part.replace('[', '').replace(']', '')
            out_file = font.replace(".ttf", "-subset-{}.woff2".format(subset_id))
            in_path = os.path.join(source_dir, font)
            out_path = os.path.join(files_dir, out_file)
            # subset css
            css_part = (
                "/* {} [{}] */\n".format(font_family, subset_id),
                "@font-face {\n",
                "  font-family: '{}';\n".format(font_family),
                "  font-style: normal;\n",
                "  font-weight: {};\n".format(font_weight),
                "  font-display: swap;\n",
                "  src: url('./files/{}') format('woff2');\n".format(out_file),
                "  unicode-range: {}\n".format(unicode),
                "}\n"
            )
            css += "".join(css_part)
            # subset font
            args = [
                in_path,
                "--output-file={}".format(out_path),
                "--flavor=woff2",
                "--unicodes={}".format(unicode),
                "--passthrough-tables",
            ]
            tasks.append((out_file, args))
        # save css file
        css_filename = font.replace(".ttf", ".css")
        css_path = os.path.join(package_dir(package), css_filename)
        with open(css_path, 'w', newline='\n') as f:
            f.write(css)
        main_css += "@import url('./{}');\n".format(css_filename)
    # save main css file
    main_css_filename = "style.css"
    main_css_path = os.path.join(package_dir(package), main_css_filename)
    with open(main_css_path, 'w', newline='\n') as f:
        f.write(main_css)
    # subset fonts in parallel
    with Pool(4) as pool:
        pool.map(subset_worker, tasks)

def update_version(package, version):
    version_file = os.path.join(package_dir(package), "VERSION")
    with open(version_file, 'w', newline='\n') as f:
        f.write(version)

def subset_worker(task):
    out_file, args = task
    print("Generating {}".format(out_file))
    main(args)

if __name__ == '__main__':
    args = sys.argv[1:]

    if "--package" in args:
        package = args[args.index("--package") + 1]
        if package not in PACKAGES:
            print("Invalid package: {}".format(package))
            sys.exit(1)
        should_update, latest_version = diff_version(package)
        print("Packaging {} version {}".format(
                    package, latest_version))
        download_assets(package)
        build_npm_package(package)
    else:
        for package in PACKAGES:
            should_update, latest_version = diff_version(package)
            if should_update:
                print("Updating {} to {}".format(package, latest_version))
                update_version(package, latest_version)
            else:
                print("{} is up to date".format(package))
