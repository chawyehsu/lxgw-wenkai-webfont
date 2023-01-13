lxgw-wenkai-webfont
===================

> A webfont package for the LXGW WenKai typeface.

[![demo][demo-badge]][demo-url] [![npm][npm-badge]][npm-url] [![npm][license-badge]](LICENSE) [![npm][npm-dl-badge]][npm-url] [![jsdelivr][jsdelivr-badge]][jsdelivr-url]

For more information about the typeface, see [LXGW WenKai's website][lxgw-wenkai].

## Usage

#### Use NPM

First, install the package via npm or yarn.

```sh
npm install --save lxgw-wenkai-webfont
# or Lite version
npm install --save lxgw-wenkai-lite-webfont
# or TC version
npm install --save lxgw-wenkai-tc-webfont
# or Screen version
npm install --save lxgw-wenkai-screen-webfont
```

Then import `style.css` to your main css style file and update the font-family.

```css
@import 'lxgw-wenkai-webfont/style.css';
/* Lite version */
@import 'lxgw-wenkai-lite-webfont/style.css';
/* TC version */
@import 'lxgw-wenkai-tc-webfont/style.css';
/* Screen version */
@import 'lxgw-wenkai-screen-webfont/style.css';
body {
  font-family: "LXGW WenKai", sans-serif;
  /* Lite version */
  font-family: "LXGW WenKai Lite", sans-serif;
  /* TC version */
  font-family: "LXGW WenKai TC", sans-serif;
  /* Screen version */
  font-family: "LXGW WenKai Screen", sans-serif;
}

/* Mono font (optional) */
pre,code {
  font-family: "LXGW WenKai Mono", sans-serif;
  /* Lite version */
  font-family: "LXGW WenKai Mono Lite", sans-serif;
  /* TC version */
  font-family: "LXGW WenKai Mono TC", sans-serif;
}
```

#### Use CDN

Put the jsDelivr `<link>` into your html head, then update the font-family.

```html
<html>
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.1.0/style.css" />
  <!-- Lite version -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-lite-webfont@1.1.0/style.css" />
  <!-- TC version -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-tc-webfont@1.0.0/style.css" />
  <!-- Screen version -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-screen-webfont@1.1.0/style.css" />
  <style>
    body {
      font-family: "LXGW WenKai", sans-serif;
      /* Lite version */
      font-family: "LXGW WenKai Lite", sans-serif;
      /* TC version */
      font-family: "LXGW WenKai TC", sans-serif;
      /* Screen version */
      font-family: "LXGW WenKai Screen", sans-serif;
    }
  </style>
</head>
<body>
  <!-- blablabla -->
</body>
</html>
```

The following are some `cdnjs` mirrors for mainland China, which have high service stability and low latency.
  + `cdn.bootcdn.net`
  + `www.staticfile.org`
  + `cdn.baomitu.com`
  + ...
```html
<!-- example of mirror cdn.bootcdn.net-->
<link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/lxgw-wenkai-webfont/1.6.0/style.min.css" />
<link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/lxgw-wenkai-screen-webfont/1.6.0/style.min.css" />
```
**Attention**: **ONLY** webfont `LXGW WenKai` and its screen version `LXGW WenKai Screen` are available at `cdnjs`, whose version is both the latest `1.6.0`. So are the mirrors.

#### Use specific font weights

You can also include specific weights if you don't want to use all the font
weights or don't want to use mono font. For example:

```css
@import 'lxgw-wenkai-webfont/lxgwwenkai-regular.css';
@import 'lxgw-wenkai-webfont/lxgwwenkai-bold.css';
body {
  font-family: "LXGW WenKai", sans-serif;
}
```

Lite version and TC version also support the same way. To know what css modules
are available, please check out the npm package.

## License

**lxgw-wenkai-webfont** © [Chawye Hsu](https://github.com/chawyehsu). Released under the [MIT](LICENSE) License.  
The LXGW WenKai typeface is available under the [SIL Open Font License 1.1][ofl] license.

> [Blog](https://chawyehsu.com) · GitHub [@chawyehsu](https://github.com/chawyehsu) · Twitter [@chawyehsu](https://twitter.com/chawyehsu)


[demo-badge]: https://img.shields.io/badge/online-demo-blue.svg?style=flat-square
[demo-url]: https://chawyehsu.github.io/lxgw-wenkai-webfont
[npm-badge]: https://img.shields.io/npm/v/lxgw-wenkai-webfont.svg?style=flat-square
[npm-url]: https://www.npmjs.com/package/lxgw-wenkai-webfont
[license-badge]: https://img.shields.io/npm/l/lxgw-wenkai-webfont.svg?style=flat-square
[license-url]: LICENSE
[npm-dl-badge]: https://img.shields.io/npm/dt/lxgw-wenkai-webfont.svg?style=flat-square
[lxgw-wenkai]: https://github.com/lxgw/LxgwWenKai
[jsdelivr-badge]: https://data.jsdelivr.com/v1/package/npm/lxgw-wenkai-webfont/badge
[jsdelivr-url]: https://www.jsdelivr.com/package/npm/lxgw-wenkai-webfont
[ofl]: https://scripts.sil.org/OFL
