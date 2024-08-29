import { expect, test } from "@playwright/test";
import sitemap from "../../docs/build/html/pages.json";

const PAGES = sitemap.urlset.url.map((url) =>
  url.loc.replaceAll(/\/index.html$/g, "."),
);

PAGES.forEach((path) => {
  test.describe(path, () => {
    test("matches the saved screenshot", async ({ page }) => {
      await page.goto(path);
      await expect(page).toHaveScreenshot(
        [path.replaceAll(/(^\/|\/$)/g, ""), "screenshot.png"],
        { fullPage: true },
      );
    });
  });
});

test.describe("@mobile menu", () => {
  test("matches the saved screenshot", async ({ page }) => {
    await page.goto("/");
    await page.getByRole("button", { name: "Menu" }).click();
    await expect(page).toHaveScreenshot("screenshot-menu-open.png");
  });
});
