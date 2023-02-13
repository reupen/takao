const cssnano = require("cssnano");
const postcssPresetEnv = require("postcss-preset-env");
const atImport = require("postcss-import");
const postcssCustomMedia = require("postcss-custom-media");

module.exports = {
  plugins: [
    atImport(),
    postcssCustomMedia(),
    postcssPresetEnv({ stage: 1 }),
    cssnano({
      preset: "default",
    }),
  ],
};
