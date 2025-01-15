// JavaScript function to handle screen size-based scaling
function handlePageScaling() {
  const width = window.innerWidth;

  if (width >= 992 && width <= 1600) {
    document.body.style.transform = "scale(0.9)";
    document.body.style.transformOrigin = "top center";
  } else if (width >= 700 && width <= 767) {
    document.body.style.transform = "scale(0.8)";
    document.body.style.transformOrigin = "top center";
  } else if (width >= 600 && width <= 700) {
    document.body.style.transform = "scale(0.75)";
    document.body.style.transformOrigin = "top center";
  } else if (width <= 600) {
    document.body.style.transform = "scale(0.5)";
    document.body.style.transformOrigin = "top center";
  } else {
    document.body.style.transform = "scale(1)";
    document.body.style.transformOrigin = "top center";
  }
}

handlePageScaling();

window.addEventListener("resize", handlePageScaling);
