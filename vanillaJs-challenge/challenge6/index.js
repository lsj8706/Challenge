// <⚠️ DONT DELETE THIS ⚠️>
//import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>
const title = document.querySelector("h2");
const range = document.querySelector(".js-range");
const span = document.querySelector("span");
const gameResult = document.querySelector("h3");
const input = document.getElementById("js-guess");
const btn = document.getElementById("js-btn");

function result(mynum, randnum) {
  if (parseInt(mynum) === randnum) {
    gameResult.innerText = "You Win!";
  } else {
    gameResult.innerText = "You Lost!";
  }
}

function play(event) {
  event.preventDefault();
  const rangeValue = range.value;
  const inputNumber = input.value;
  let randomNumber = Math.floor(Math.random() * (rangeValue - 1)) +1;
  console.log(randomNumber);
  span.innerText = `You chose: ${inputNumber}, the machine chose:${randomNumber}`;
  result(inputNumber, randomNumber);
}

function loadTitle() {
  const rangeValue = range.value;
  title.innerText = `Generate a number between 0 and ${rangeValue}`;
}

function init() {
  loadTitle();
  range.addEventListener("change", loadTitle);
  btn.addEventListener("click", play);
}
init();
