document.addEventListener("DOMContentLoaded", () => {
  const toggleBtn = document.querySelector(".toggle-btn");
  const leftMenu = document.querySelector(".left-menu");

  toggleBtn.addEventListener("click", () => {
    leftMenu.classList.toggle("collapsed");
  });

  function adjustPageSize() {
    const width = window.innerWidth;

    if (width >= 992 && width <= 1600) {
      document.body.style.zoom = "0.9";
    } else if (width >= 700 && width <= 767) {
      document.body.style.zoom = "0.8";
    } else if (width >= 600 && width <= 700) {
      document.body.style.zoom = "0.75";
    } else if (width <= 600) {
      document.body.style.zoom = "0.5";
    } else {
      document.body.style.zoom = "1";
    }
  }

  window.addEventListener("resize", adjustPageSize);
  adjustPageSize();
});
