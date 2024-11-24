/**
 * Main JS file for BPDev behaviours
 */

// Menu on small screens
let menuToggle = document.querySelectorAll(".menu-toggle");
if (menuToggle) {
  for (let i = 0; i < menuToggle.length; i++) {
    menuToggle[i].addEventListener(
      "click",
      function (e) {
        document.body.classList.toggle("menu--opened");
        e.preventDefault();
      },
      false,
    );
  }
}

function loadLanguage(lang) {
  let base_pathname = window.location.pathname;
  // ISO 639-1 language codes are two-letter codes
  // ISO 3166-1 alpha-2 country codes are two-letter codes
  let lang_path_regex = /^\/[a-z]{2}([_-][A-Z]{2})?\//;

  // Check if the URL path is more than just /path/ and starts with a language code
  let path_parts = base_pathname.split("/");
  let isLongPath = path_parts.length >= 3;
  let startsWithLangCode = lang_path_regex.test(base_pathname);

  if (isLongPath && startsWithLangCode) {
    base_pathname = base_pathname.replace(lang_path_regex, "/");
  }

  let url = lang !== "en" ? "/" + lang + base_pathname : base_pathname;

  window.location.assign(url);
}

$(document).ready(function () {
  $("#language").change(function () {
    loadLanguage($("#language option:selected").val());
  });
});

let currentIndex = 0;

function moveSlide(direction) {
  const slides = document.querySelector(".slides");
  const totalSlides = slides.children.length;

  currentIndex += direction;

  if (currentIndex < 0) {
    currentIndex = totalSlides - 1;
  } else if (currentIndex >= totalSlides) {
    currentIndex = 0;
  }

  slides.style.transform = `translateX(-${currentIndex * 100}%)`;
}
