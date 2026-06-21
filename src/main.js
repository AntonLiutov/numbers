import { generateRandomNumber } from "./random-number.js";

const button = document.querySelector("#generate-button");
const numberValue = document.querySelector("#number-value");
const numberStatus = document.querySelector("#number-status");

function updateDisplayedNumber(value) {
  numberValue.classList.add("is-updating");

  window.setTimeout(() => {
    numberValue.textContent = String(value);
    numberValue.classList.remove("is-updating");
    numberValue.classList.add("has-value");
    numberStatus.textContent = "Generated instantly in your browser.";
  }, 90);
}

button?.addEventListener("click", () => {
  const nextValue = generateRandomNumber();
  updateDisplayedNumber(nextValue);
});
