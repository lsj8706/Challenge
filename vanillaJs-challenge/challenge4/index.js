// <⚠️ DONT DELETE THIS ⚠️>
//import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>
const select = document.querySelector("select");
const option = select.querySelector("option");
const korea = option.querySelector("korea"),
  greece = option.querySelector("greece"),
  turkey = option.querySelector("turkey"),
  finland = option.querySelector("finland");
const COUNTRY = "country";

function saveCountry(text) {
  localStorage.setItem(COUNTRY, text);
}

function hanleSelect(event) {
  event.preventDefault();
  const currentValue = select.options[select.selectedIndex].value;
  saveCountry(currentValue);
}

function askForCountry() {
  select.addEventListener("change", hanleSelect);
}
function printCountry(text) {
   const check = select.querySelector(`option[value=${text}]`);
   check.setAttribute("selected",true);
}

function loadCountry() {
  const currentCountry = localStorage.getItem(COUNTRY);
  if (currentCountry === null) {
    askForCountry();
  } else {
    printCountry(currentCountry);
  }
}

function init() {
  loadCountry();
}
init();
