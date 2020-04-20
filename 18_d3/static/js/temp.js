var margin = {top: 100, left: 100};
var width = 1000 - margin.left;
var height = 500 - margin.top;
var country_idx = 0
var country = ["Bangladesh", "China", "France", "India", "Ireland", "Philippines", "United States", "World"]
// var curtain_offset = 200;
var c;
var valueline

var svg;

// set the ranges
var x = d3.scaleLinear().range([0, 800]);
var y = d3.scaleLinear().range([height, 0]);

/*
function x(input) {
  return (width - 0) * input;
}

function y(input) {
  return (0 - height) * input;
}
*/
// define the line
// console.log("d." + "Population_" + country_idx + " = +d." + "Population_" + country_idx)
var something = function(){
    svg = d3.select("body").append("svg")
    .attr("width", width + margin.left)
    .attr("height", height + margin.top)
    .append("g")
    .attr("transform",
    "translate(" + margin.left + ",0)");
    valueline = d3.line()

        .x(function(d) { return x(d.Year); })
        .y(function(d) { return y(eval("d." + "Population_" + country_idx + "= +d." + "Population_" + country_idx)) });


    // Get the data
    d3.csv("static/csv/test.csv").then(function(data) {

      // format the data
      data.forEach(function(d) {
          d.Year = +d.Year;
          eval("d." + "Population_"+country_idx + "= +d." + "Population_"+country_idx);
      });
      // Scale the range of the data
      x.domain(d3.extent(data, function(d) { return d.Year; }));
      y.domain([0, d3.max(data, function(d) { return eval("d." + "Population_"+country_idx + "= +d." + "Population_"+country_idx) })]);

      // Add the valueline path.
      svg.append("path")
          .data([data])
          .attr("class", "line")
          .attr("d", valueline);

      // Add the x Axis
      svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));
      svg.append("text")
         .attr("transform",
               "translate(" + 350 + " ," +
                              470 + ")")
         .style("text-anchor", "middle")
         .text("Year");
      // Add the y Axis
      svg.append("g")
      .call(d3.axisLeft(y));
      svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x",0 - (height / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Population");
    });

}
var animation_id;

var render_graph = function() {
  let left = +c.style("left").slice(0, c.style("left").length - 2);
  let width = +c.style("width").slice(0, c.style("width").length - 2);

  let change_factor = 8;

  c.style("left", left + change_factor);
  c.style("width", width - change_factor);

  if (left < 2000)
    animation_id = window.requestAnimationFrame(render_graph);
  else {
    window.cancelAnimationFrame(animation_id);
  }
}

var transition = function() {
    if (country_idx >= 7){
        country_idx = 0;
    }
    else {
        country_idx++;
    }
    var h = document.getElementById("h");
    h.innerHTML = "Population of " + country[country_idx];
    d3.select("svg").remove();


}


var btn_r = document.getElementById("render");
var btn_t = document.getElementById("transition");
btn_r.addEventListener("click", something);
btn_t.addEventListener("click", transition);
