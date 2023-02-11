function updatePageNav() {
  const items = document.querySelectorAll("a.page-nav-link");

  let current: Element;
  for (const [index, item] of Array.from(items).entries()) {
    const targetSelector = item.getAttribute("href");

    if (!targetSelector) {
      continue;
    }

    const target = document.querySelector(targetSelector);

    if (!target) {
      continue;
    }

    const rect = target.getBoundingClientRect();

    if (rect.top >= 0 || (index + 1 === items.length && rect.bottom >= 0)) {
      current = item;
      item.classList.add("current");
      break;
    }
  }

  items.forEach((item) => {
    if (item !== current) {
      item.classList.remove("current");
    }
  });
}

function initSidebar() {
  const sidebar = document.querySelector(".sidebar-container");
  const menuButton = document.getElementById("toggle-menu");
  const blurOverlay = document.getElementById("blur-overlay");

  if (!sidebar || !menuButton || !blurOverlay) {
    return;
  }

  const openSidebar = () => {
    sidebar.classList.add("open");
    document.documentElement.classList.add("overlay-active");
    menuButton.setAttribute("aria-expanded", "true");
    menuButton.setAttribute("aria-label", "Expand sidebar");
    blurOverlay.removeAttribute("hidden");
    document.addEventListener("click", handleDocumentClick, { capture: true });
  };

  const closeSidebar = () => {
    sidebar.classList.remove("open");
    document.documentElement.classList.remove("overlay-active");
    menuButton.setAttribute("aria-expanded", "false");
    menuButton.setAttribute("aria-label", "Collapse sidebar");
    blurOverlay.setAttribute("hidden", "hidden");
    document.removeEventListener("click", handleDocumentClick, { capture: true });
  };

  const handleDocumentClick = (event: MouseEvent) => {
    if ((event.target instanceof Element && sidebar.contains(event.target))) {
      return;
    }

    closeSidebar();
    event.stopPropagation();
    event.preventDefault();
  };

  const handleMenuButtonClick = () => {
    if (!sidebar.classList.contains("open")) {
      openSidebar();
    }
  };

  menuButton.addEventListener("click", handleMenuButtonClick);
}

document.addEventListener("scroll", updatePageNav);
updatePageNav();

initSidebar();
