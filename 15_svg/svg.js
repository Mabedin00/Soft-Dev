
var button_clear = document.getElementById("clear");
var button_move = document.getElementById("move");
var button_xtra = document.getElementById("xtra");
var pic = document.getElementById("vimage");
var animation_id;
let c;
var clear = function(e) {
	e.preventDefault();
    while (pic.lastChild) {
        pic.removeChild(pic.lastChild);
    }
	window.cancelAnimationFrame(animation_id);

};


var plot = function(e) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
	if(e.target.getAttribute("id") == "vimage"){
	    c.setAttribute("cx", e.offsetX);
	    c.setAttribute("cy", e.offsetY);
	    c.setAttribute("r", "25");
		c.setAttribute("dx", 1);
		c.setAttribute("dy", 1);
		c.setAttribute("dr", 1);
	    c.setAttribute("fill", "blue");
	    c.setAttribute("stroke", "black");
	    pic.appendChild(c);
	}
};

var move = function(e){
	var children = pic.children;
	for (var i = 0; i < children.length; i++) {

		x =  parseInt(children[i].getAttribute("cx"));
		y =  parseInt(children[i].getAttribute("cy"));
		dx = parseInt(children[i].getAttribute("dx"));
		dy = parseInt(children[i].getAttribute("dy"));
		r =  parseInt(children[i].getAttribute("r") );

		children[i].setAttribute("cx", x + dx);
		children[i].setAttribute("cy", y + dy);

		if (x < r || x > pic.getAttribute("width") - r) {
			children[i].setAttribute("dx", -dx);
			children[i].setAttribute("cx", x - dx * 3);
		}
		if (y < r || y > pic.getAttribute("height") - r) {
			children[i].setAttribute("dy", -dy);
			children[i].setAttribute("cy", y - dy * 3);
		}
	}
	animation_id = window.requestAnimationFrame(move);
};

var xtra = function(e) {
	var children = pic.children;
	colors =  ["AliceBlue", "Aqua", "BlueViolet", "Chartreuse", "CornflowerBlue",
			   "Chocolate", "DarkBlue", "DarkOrchid", "Fuchsia", "Indigo",
			   "LightGreen", "MediumOrchid", "Lime", "MediumSpringGreen", "Tomato"]
    for (var i = 0; i < children.length; i++) {
	    children[i].setAttribute("fill", colors[Math.floor(Math.random()*15)]);
    }
    animation_id = window.requestAnimationFrame(xtra);

};

var stop_animation = function(e) {
	window.cancelAnimationFrame(animation_id);
};





button_clear.addEventListener("click", clear);
button_move.addEventListener("click", move);
button_xtra.addEventListener("click", xtra);
pic.addEventListener("click", plot)
