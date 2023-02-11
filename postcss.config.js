const postcssPresetEnv = require("postcss-preset-env");
const atImport = require("postcss-import");
const postcssCustomMedia = require("postcss-custom-media");
const path = require("node:path");
const url = require("postcss-url");

module.exports = {
  plugins: [
    atImport(),
    postcssCustomMedia(),
    postcssPresetEnv({ stage: 1 }),
    // url({
    //     url: "copy",
    // basePath: path.resolve('node_modules/inter-ui'),
    // // dir to copy assets
    // assetsPath: 'static',
    // // using hash names for assets (generates from asset content)
    // useHash: true
    //}),
    require("cssnano")({
      preset: "default",
    }),
  ],
};
