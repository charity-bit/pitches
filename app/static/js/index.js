const header = document.querySelector("header");
const show = document.querySelector(".show");
const hide = document.querySelector(".hide");

show.addEventListener("click", () => {
  header.style.display = "flex";
});

hide.addEventListener("click", () => {
  header.style.display = "none";
});
