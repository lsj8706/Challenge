// <⚠️ DONT DELETE THIS ⚠️>
//import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>
const toDoForm = document.querySelector(".js-toDoForm"),
  toDoInput = toDoForm.querySelector("input"),
  toDoList = document.querySelector(".js-toDoList"),
  finishedList = document.querySelector(".js-finishedList");
const PENDING_LS = "PENDING";
const FINISHED_LS = "FINISHED";
let toDos = [];
let finishedDos = [];
let idNumbers = 1;
let idNumbers2 = 1;
function saveToDos() {
  localStorage.setItem(PENDING_LS, JSON.stringify(toDos));
}
function savefinishedDos() {
  localStorage.setItem(FINISHED_LS, JSON.stringify(finishedDos));
}

function deleteToDo(event) {
  const btn = event.target;
  const li = btn.parentNode;
  toDoList.removeChild(li);
  const cleanToDos = toDos.filter(function (toDo) {
    return toDo.id !== parseInt(li.id);
  });
  toDos = cleanToDos;
  saveToDos();
}
function deleteFinished(event) {
  const btn = event.target;
  const li = btn.parentNode;
  finishedList.removeChild(li);
  const cleanfinished = finishedDos.filter(function (toDo) {
    return toDo.id !== parseInt(li.id);
  });
  finishedDos = cleanfinished;
  savefinishedDos();
}

function addFinishToDo(event) {
  const btn = event.target;
  const li = btn.parentNode;
  console.log(li.querySelector("span").innerText);
  const text = li.querySelector("span").innerText;
  btn.innerText = "⏪";
  toDoList.removeChild(li);
  paintFinished(text);
  const removedToDos = toDos.filter(function (toDo) {
    return toDo.id !== parseInt(li.id);
  });
  toDos = removedToDos;
  saveToDos();
}

function backToDo(event) {
  const btn = event.target;
  const li = btn.parentNode;
  console.log(li.querySelector("span").innerText);
  const text = li.querySelector("span").innerText;
  btn.innerText = "✔";
  finishedList.removeChild(li);
  paintToDo(text);
  const removedFinished = finishedDos.filter(function (toDo) {
    return toDo.id !== parseInt(li.id);
  });
  finishedDos = removedFinished;
  savefinishedDos();
}

function paintToDo(text) {
  const li = document.createElement("li");
  const delBtn = document.createElement("button");
  const finishBtn = document.createElement("button");
  const span = document.createElement("span");
  const newId = idNumbers2;
  delBtn.innerText = "❌";
  delBtn.addEventListener("click", deleteToDo);
  finishBtn.innerText = "✔";
  finishBtn.addEventListener("click", addFinishToDo);
  span.innerText = text;
  li.appendChild(span);
  li.appendChild(delBtn);
  li.appendChild(finishBtn);
  li.id = newId;
  toDoList.appendChild(li);
  const toDoObj = {
    text: text,
    id: newId
  };
  idNumbers2 += 1;
  toDos.push(toDoObj);
  saveToDos();
}
function paintFinished(text) {
  const li = document.createElement("li");
  const delBtn = document.createElement("button");
  const backBtn = document.createElement("button");
  const span = document.createElement("span");
  const newId = idNumbers;
  delBtn.innerText = "❌";
  delBtn.addEventListener("click", deleteFinished);
  backBtn.innerText = "⏪";
  backBtn.addEventListener("click", backToDo);
  span.innerText = text;
  li.appendChild(span);
  li.appendChild(delBtn);
  li.appendChild(backBtn);
  li.id = newId;
  finishedList.appendChild(li);
  const finishedObj = {
    text: text,
    id: newId
  };
  idNumbers += 1;
  finishedDos.push(finishedObj);
  savefinishedDos();
}

function handleSubmit(event) {
  event.preventDefault();
  const currentValue = toDoInput.value;
  paintToDo(currentValue);
  toDoInput.value = "";
}

function loadToDos() {
  const loadedPending = localStorage.getItem(PENDING_LS);

  if (loadedPending !== null) {
    const parsedPending = JSON.parse(loadedPending);
    console.log(parsedPending);
    parsedPending.forEach(function (toDo) {
      paintToDo(toDo.text);
    });
  }
}
function loadFinished() {
  const loadedFinished = localStorage.getItem(FINISHED_LS);
  if (loadedFinished !== null) {
    const parsedFinished = JSON.parse(loadedFinished);
    console.log(parsedFinished);
    parsedFinished.forEach(function (toDo) {
      paintFinished(toDo.text);
    });
  }
}

function init() {
  loadToDos();
  loadFinished();
  toDoForm.addEventListener("submit", handleSubmit);
}

init();
