const cssnano = require("cssnano");
const postcssPresetEnv = require("postcss-preset-env");
const atImport = require("postcss-import");
const postcssCustomMedia = require("postcss-custom-media");
const postcssUrl = require("postcss-url");
const path = require("node:path");

module.exports = {
  plugins: [
    atImport(),
    postcssUrl({
      url: "copy",
      basePath: path.resolve(__dirname, "node_modules", "inter-ui"),
      assetsPath: "inter-ui",
      useHash: true,
    }),
    postcssCustomMedia(),
    postcssPresetEnv({ stage: 1 }),
    cssnano({
      preset: "default",
    }),
  ],
};
