// A formatter for counts.
var formatCount = d3.format(",.0f");

var margin = {top: 10, right: 30, bottom: 30, left: 30};

function update_graph(element, data) {
    var width = $(element).width() - margin.left - margin.right,
        height = $(element).height() - margin.top - margin.bottom;

    var x = d3.scale.linear()
        .domain([0, 1])
        .range([0, width]);

    var x = d3.time.scale.utc()
        .domain([d3.min(data, function (d) { return new Date(d.period_start); }),
                d3.max(data, function (d) { return new Date(d.period_end); })])
        .range([0, width]);

    var y = d3.scale.linear()
        .domain([0, d3.max(data, function(d) { return d.count; })])
        .range([height, 0]);

    var bar = d3.select(element).select("svg").selectAll(".bar")
        .data(data);

    bar.select("text")
        .attr("x", function (d) { return (x(new Date(d.period_end)) - x(new Date(d.period_start))) / 2; })
        .text(function(d) { return formatCount(d.count ? d.count : 0); });

    bar.select("rect")
        .attr("x", 0)
        .transition()
        .attr("width", function (d) { return (x(new Date(d.period_end)) - x(new Date(d.period_start))) - 1; })
        .attr("height", function(d) { return height - y(d.count ? d.count : 0); });

    bar.transition()
        .attr("transform", function(d) { return "translate(" + new Integer(x(new Date(d.period_start))) + "," + y(d.count ? d.count : 0) + ")"; });
}

function setup_graph(element, data) {
    var width = $(element).width() - margin.left - margin.right,
        height = $(element).height() - margin.top - margin.bottom;

    var x = d3.scale.linear()
        .domain([0, 1])
        .range([0, width]);

    var x = d3.time.scale.utc()
        .domain([d3.min(data, function (d) { return new Date(d.period_start); }),
                d3.max(data, function (d) { return new Date(d.period_end); })])
        .range([0, width]);

    var y = d3.scale.linear()
        .domain([0, d3.max(data, function(d) { return d.count; })])
        .range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var svg = d3.select(element).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var bar = svg.selectAll(".bar")
        .data(data)
        .enter().append("g")
        .attr("class", "bar")
        .attr("transform", function(d) { return "translate(" + x(new Date(d.period_start)) + "," + y(d.count ? d.count : 0) + ")"; });

    bar.append("rect")
        .attr("x", 0)
        .attr("width", function (d) { return (x(new Date(d.period_end)) - x(new Date(d.period_start))) - 1; })
        .attr("height", function(d) { return height - y(d.count ? d.count : 0); });

    bar.append("text")
        .attr("dy", ".75em")
        .attr("y", 6)
        .attr("x", function (d) { return (x(new Date(d.period_end)) - x(new Date(d.period_start))) / 2; })
        .attr("text-anchor", "middle")
        .text(function(d) { return formatCount(d.count ? d.count : 0); });

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

}

function setup_event_graph(element, data, obj_name) {
    var width = $(element).width() - margin.left - margin.right,
        height = $(element).height() - margin.top - margin.bottom;

    var x = d3.scale.linear()
        .domain([0, 1])
        .range([0, width]);

    var x = d3.time.scale.utc()
        .domain([d3.min(data, function (d) { return new Date(d.period_start); }),
                d3.max(data, function (d) { return new Date(d.period_end); })])
        .range([0, width]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var svg = d3.select(element).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var bar = svg.selectAll(".bar")
        .data(data)
        .enter().append("g")
        .attr("class", "bar")
        .attr("transform", function(d) { return "translate(" + x(new Date(d.period_start)) + ",0)"; });

    var rect_margin = 5;
    bar.append("rect")
        .attr("x", rect_margin)
        .attr("y", rect_margin)
        .attr("width", function (d) { return (x(new Date(d.period_end)) - x(new Date(d.period_start))) - rect_margin; })
        .attr("height", function (d) { return (x(new Date(d.period_end)) - x(new Date(d.period_start))) - rect_margin; });
        //.attr("height", function(d) { return 100 - rect_margin }); // d[obj_name] ? 100 : 200 });

    bar.append("text")
        .attr("dy", ".75em")
        .attr("y", 6)
        .attr("x", function (d) { return (x(new Date(d.period_end)) - x(new Date(d.period_start))) / 2; })
        .attr("text-anchor", "middle")
        .text(function(d) { return d[obj_name]; });

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

}
