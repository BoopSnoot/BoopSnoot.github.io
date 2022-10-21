function createContainer() {
  let newWrap = document.createElement("div");
  let containerId = "wrap" + $(".wrap").length;

  newWrap.innerHTML = $("#template").html();
  newWrap.classList.add("wrap");
  newWrap.addEventListener("click", ev => newWrap.remove());
  newWrap.setAttribute("data-tooltip", "Remove");
  newWrap.id = containerId;

  $(".div-table-content").append(newWrap);
  return containerId;
}

function removeContainer(containerId) {
  $(`#${containerId}`).remove();
}

function getProductsPrices(codes) {
  for (let code of codes.split(",")) {
    if (!/^([0-9]{1,4})$/.test(code)) continue;
    fetch(`https://xlineparts.com/product/${code}/a`).then(r =>
      r.text().then(webpage => {
        try {
          let price = webpage.match(/(?<=(<span class="price">\s{0,}))[\S]+(?=€(\s{0,})<\/span>)/)[0].trim();
          let containerId = createContainer();

          populateLabel(price, code, containerId);
        } catch (e) {
          document.body.innerHTML = "<h1 style=\"color: red\">please install <a href=\"https://chrome.google.com/webstore/detail/cors-unblock/lfhmikememgdcahcdlaciloancbhjino/\">Access Control-Allow-Origin - Unblock<\/a><\/h1>";
        }
      })
    ).catch(err => {
      document.body.innerHTML = "<h1 style=\"color: red\">please install <a href=\"https://chrome.google.com/webstore/detail/cors-unblock/lfhmikememgdcahcdlaciloancbhjino/\">Access Control-Allow-Origin - Unblock<\/a><\/h1>";
    });
  }
}

function populateLabel(price, code, containerId) {
  $(`#${containerId} .price`).text(price + "€");
  $(`#${containerId} .code`).text(code);
}
