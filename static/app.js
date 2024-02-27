const canvas = document.getElementById("myCanvas");
const output = document.querySelector(".output");
const ctx = canvas.getContext("2d");

ctx.strokeStyle = "black";

// Setting canvas dimensions
canvas.width = 600;
canvas.height = 400;

ctx.lineWidth = 15;

// Drawing on canvas
var isDrawing = false;

canvas.addEventListener("mousedown", function(event) {
  isDrawing = true;
  ctx.beginPath();
  ctx.moveTo(event.offsetX, event.offsetY);
});

canvas.addEventListener("mousemove", function(event) {
  if (isDrawing) {
    ctx.lineTo(event.offsetX, event.offsetY);
    ctx.stroke();
  }
});

window.addEventListener("mouseup", function() {
  isDrawing = false;
  ctx.closePath();
});

// Reset button
const res = document.getElementById("reset");

res.addEventListener("click", function() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    output.innerHTML = "";
});

// Brush color
const color = document.getElementById("colorpicker");

// Canvas color
const color2 = document.getElementById("colorpicker2")

window.addEventListener("click", function() {
    ctx.strokeStyle = color.value;
    canvas.style.backgroundColor = color2.value;
});

ctx.strokeStyle = color.value;
canvas.style.backgroundColor = color2.value;

// Uploading image on canvas
const input = document.getElementById('img');

input.addEventListener('change', () => {
  isDrawing = false;
  const file = input.files[0];

  const image = new Image();
  image.src = URL.createObjectURL(file);

  image.onload = () => {
    canvas.getContext('2d').drawImage(image, 0, 0, image.width, image.height, 0, 0, canvas.width, canvas.height);
  };
});

// Predict button functionality
const predict = document.querySelector(".predict");
predict.addEventListener("click", function() {
  fetch('/predict', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      }
  })
  .then(response => response.json())
  .then(data => {
      console.log(data);
      output.innerHTML = "Predicted Digit: " + data.result;
  });
});
