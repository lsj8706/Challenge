
// You're gonna need this
const title = document.querySelector("h2");

function getTime() {
  // Don't delete this.
  const xmasDay = new Date("2021-12-24:00:00:00+0900");
  const nowDate = new Date().getTime();
  const dDay = xmasDay - nowDate;
  const days = Math.floor(dDay / (1000 * 60 * 60 * 24));
  const hours = Math.floor((dDay % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((dDay % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((dDay % (1000 * 60)) / 1000);

  title.innerHTML = `${days}d ${hours < 10 ? `0${hours}` : hours}h ${
    minutes < 10 ? `0${minutes}` : minutes
  }m ${seconds < 10? `0${seconds}`:seconds}s`;

}

function init() {
  getTime();
  setInterval(getTime, 1000);
}
init();
