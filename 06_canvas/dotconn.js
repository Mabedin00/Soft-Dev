// Mo Abedin
// SoftDev1 pd2
// K06 -- ...and I want to Paint It Better
// 2020-02-06
var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");
var button = document.getElementById("clear");

var prevX;
var prevY;

var clear = function(e) {
	e.preventDefault();
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	prevX = -1;
};

var plot = function(e) {
	if (prevX == -1) {
		prevX = e.offsetX;
		prevY = e.offsetY;
	}
	ctx.beginPath();
    ctx.arc(e.offsetX, e.offsetY, 5, 0, 2 * Math.PI);
    ctx.fill();
    ctx.closePath();

    ctx.beginPath();

    ctx.moveTo(prevX, prevY);
    ctx.lineTo(e.offsetX, e.offsetY);

    ctx.stroke();
    ctx.closePath();

    prevX = e.offsetX;
    prevY = e.offsetY;
};

button.addEventListener("click", clear);
canvas.addEventListener("click", plot);
