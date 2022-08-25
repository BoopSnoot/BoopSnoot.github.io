let idInput = document.getElementById("id");
let button = document.getElementById("button");
let iframe = document.getElementById("iframe");

idInput.addEventListener("keypress", ev => {
  if (ev.key === "Enter") button.click();
});

button.addEventListener("click", ev => {
  iframe.src = "https://xlineparts.com/product/" + document.getElementById("id").value + "/a";
});
