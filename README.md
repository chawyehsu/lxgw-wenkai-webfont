lxgw-wenkai-webfont
===================

> A webfont package for the LXGW WenKai typeface.

[![demo][demo-badge]][demo-url] [![npm][npm-badge]][npm-url] [![npm][license-badge]](LICENSE) [![npm][npm-dl-badge]][npm-url] [![jsdelivr][jsdelivr-badge]][jsdelivr-url]


For more information about the typeface, see [LXGW WenKai's website][lxgw-wenkai].

## Usage

#### Use jsDelivr

Put the jsDelivr `<link>` into your html head, then set your font-family to use `LXGW WenKai`. For example:

```html
<html>
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@0/style.min.css" />
  <style>
    body {
      font-family: "LXGW WenKai", sans-serif;
    }
  </style>
</head>
<body>
  <!-- blablabla -->
</body>
</html>
```

#### Use NPM

First, install the package via npm or yarn.

```sh
npm install --save lxgw-wenkai-webfont
```

Then import the css to your main css style file and set your font-family to use `LXGW WenKai`.

```css
@import '~lxgw-wenkai-webfont/style.css';
body {
  font-family: "LXGW WenKai", sans-serif;
}
```

## License

**lxgw-wenkai-webfont** © [Chawye Hsu](https://github.com/chawyehsu). Released under the [MIT](LICENSE) License.  
The LXGW WenKai typeface is available under the [SIL Open Font License 1.1](OFL.txt) license.

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
