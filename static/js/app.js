// AOS
AOS.init({
  duration: 700,
  easing: "ease",
  once: true,
  disable: "mobile",
});

// Products Carousel
$(".product-carousel").owlCarousel({
  loop: true,
  margin: 5,
  dots: false,
  nav: false,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 3,
    },
    1000: {
      items: 5,
    },
  },
});

// Stars
$(document)
  .on("mouseenter", ".fa-star", function () {
    $(this).removeClass("text-secondary").addClass("text-warning");
    $(this)
      .parent("div")
      .prevAll("div")
      .children("i")
      .removeClass("text-secondary")
      .addClass("text-warning");
  })
  .on("mouseleave", ".fa-star", function () {
    $(".fa-star").removeClass("text-warning").addClass("text-secondary");
  });

// Product Increase and decrease button
function increaseValue() {
  var value = parseInt(document.getElementById("number").value, 10);
  value = isNaN(value) ? 0 : value;
  value++;
  document.getElementById("number").value = value;
}

function decreaseValue() {
  var value = parseInt(document.getElementById("number").value, 10);
  value = isNaN(value) ? 0 : value;
  value < 1 ? (value = 1) : "";
  value--;
  document.getElementById("number").value = value;
}

// Splide Js Product Carousel

var currentImage;
var splide;
var previousButton, nextButton;
var thumbnails, thumbnailButtons;

window.addEventListener("DOMContentLoaded", function (e) {
  currentImage = document.querySelector(".current-image");
  previousButton = document.querySelector(".carousel .previous-button");
  nextButton = document.querySelector(".carousel .next-button");
  thumbnails = document.querySelectorAll(".carousel .thumbnail");
  thumbnailButtons = document.querySelectorAll(".carousel .thumbnail-button");

  thumbnailButtons.forEach(function (thumbnailButton) {
    thumbnailButton.addEventListener("click", function (e) {
      activateThumbnail(thumbnailButton);
    });
  });

  splide = new Splide(".splide", {
    gap: "10px",
    padding: {
      left: "25px",
      right: "25px",
    },
    arrows: false,
    perPage: 3,
    pagination: false,
    keyboard: false, // Splide listens to key events at the document level and moves ALL carousels when arrow keys are used. Also, keyboard controls are not expected by real users.
    slideFocus: false, // removes tabindex="0" from each slide wrapper, since we only want our links inside each slide to receive focus.
  }).mount();

  // To prevent animation issues, let's make every slide visible before a transition happens. Splide will then automatically remove the `.is-visible` class from non-visible slides once the transition is finished.
  splide.on("move", function () {
    var slides = document.querySelectorAll(".splide .splide__slide");

    slides.forEach(function (slide) {
      slide.classList.add("is-visible");
    });
  });

  // Go to the previous slide when the Previous button is activated
  previousButton.addEventListener("click", function (e) {
    splide.go("<");
  });

  // Go to the next slide when the Next button is activated
  nextButton.addEventListener("click", function (e) {
    splide.go(">");
  });
});

/**
  Update the large current image when a thumbnail button is activated.
*/
function activateThumbnail(thumbnailButton) {
  // Swap the current image based to match the thumbnail
  // - If you'd like to use separate images, like higher-res versions, consider using the index to pick an appropriate src string from an array, or storing the URI of the higher-res image in a custom data attribute on the thumbnail.
  var newImageSrc = thumbnailButton.querySelector("img").getAttribute("src");
  var newImageAlt = thumbnailButton
    .querySelector("img")
    .getAttribute("data-full-alt");
  currentImage.querySelector("img").setAttribute("src", newImageSrc);
  currentImage.querySelector("img").setAttribute("alt", newImageAlt);

  // Remove aria-current from any previously-activated thumbnail
  thumbnailButtons.forEach(function (button) {
    button.removeAttribute("aria-current");
  });

  // Indicate to screen readers which thumbnail is selected using aria-current
  thumbnailButton.setAttribute("aria-current", true);
}

// Zoom Image On Hover
var options1 = {
  // width: 400,
  // zoomWidth: 500,
  offset: { vertical: 0, horizontal: 10 },
};

// If the width and height of the image are not known or to adjust the image to the container of it
var options2 = {
  fillContainer: true,
  offset: { vertical: 0, horizontal: 10 },
};
new ImageZoom(document.getElementById("img-container"), options2);

// Search

const searchAny = () => {
  const header = document.querySelector(".header");
  const search = document.querySelector(".search-icon");
  const close = document.querySelector(".close");

  const clickEvent = () => {
    header.classList.toggle("search-active");
    header.classList.toggle("search-close");
  };

  search.addEventListener("click", clickEvent);
  close.addEventListener("click", clickEvent);
};

searchAny();
