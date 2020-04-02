
var button = document.getElementById("clear");
var pic = document.getElementById("vimage");
var list = []
var clear = function(e) {
	e.preventDefault();
    while (pic.lastChild) {
        pic.removeChild(pic.lastChild);
    }
    prevX = -1;

};
var plot = function(e) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
	if(e.target.getAttribute("id") == "vimage"){
	    c.setAttribute("cx", e.offsetX);
	    c.setAttribute("cy", e.offsetY);
	    c.setAttribute("r", "25");
	    c.setAttribute("fill", "blue");
	    c.setAttribute("stroke", "black");
		c.addEventListener("click", changeColor)
	    pic.appendChild(c);
	}
};

var move = function(e){
	e.target.setAttribute("fill", "blue");
	e.target.setAttribute("cx", Math.floor(Math.random() * 501));
	e.target.setAttribute("cy", Math.floor(Math.random() * 501));
	e.target.removeEventListener("click", move)
	e.target.addEventListener("click", changeColor)

};
var changeColor = function(e){
	e.target.setAttribute("fill", "cyan");
	e.target.addEventListener("click", move)

};




button.addEventListener("click", clear);
pic.addEventListener("click", plot)
