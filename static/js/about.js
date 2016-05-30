document.addEventListener("DOMContentLoaded", function(){
    var svg = document.getElementById('timeline-graphic'); //Get svg element
    //100 coords wide
    var LINE_X = 9.5;
    var START_YEAR = 2011;
    var YEAR_HEIGHT = 200;
    var TOP_PADDING = 10;
    
    //set of events, key is the dot position, value is the text
    //associated with it (optionally with positions)
    var events = {
        2016.32: "Launched Clever Badges",
        2016.15: {
            2016.18: "Began tech volunteering",
            2016.10: "at Alpha Public Schools"
        },
        2015.65: "Started playing DnD",
        2015.45: {
            2015.45: "Created the Schools",
            2015.37: "team at Clever"
        },
        2015.13: {
            2015.16: "Launched the Do",
            2015.08: "apps at IFTTT"
        },
        2014.8: {
            2014.83: "Backpaced for 9",
            2014.75: "days in Japan"
        },
        2014.35: {
            2014.41: "Ran the Boston",
            2014.33: "Marathon in 4:03"
        },
        2014.2: {
            2014.21: "Biked 220 miles",
            2014.13: "along highway 1"
        },
        2013.73: {
            2013.76: "Spoke at HPAIR",
            2013.68: "in Dubai"
        },
        2012.65: "YCS12 Demo Day",
        2012.46: "Graduated MIT",
        2012.35: {
            2012.33: "Won the MIT",
            2012.25: "$100k Competition"
        },
        2012.10: "Started Filepicker.io",
        2011.5: "Interned at Google"
    };

    function coordToY(coord) {
        var now = new Date();
        var year = now.getUTCFullYear();
        //initial is the % of the year so far
        var initial = (now - new Date(year, 0, 1))/(1000 * 3600 * 24 * 365);
        return TOP_PADDING + (initial + (year - coord)) * YEAR_HEIGHT;
    }

    function createElement(type) {
        return document.createElementNS("http://www.w3.org/2000/svg", type);
    }

    function createEventNode(coord) {
        var node = createElement("circle");
        node.setAttribute("class", "event");
        node.setAttribute("cx", LINE_X);
        node.setAttribute("cy", coordToY(coord));
        node.setAttribute("r", 3);

        svg.appendChild(node);
        return node;
    }

    function createTextElement(coord, text) {
        var node = createElement("text");
        node.setAttribute("class", "event");
        node.setAttribute("x", LINE_X + 10);
        node.setAttribute("y", coordToY(coord));
        node.appendChild(document.createTextNode(text));

        svg.appendChild(node);
        return node;
    }

    function createEvent(coord, data) {
        createEventNode(coord);
        if (typeof data === "string") {
            createTextElement(coord - 0.015, data);
        } else {
            for (var tcoord in data) {
                createTextElement(tcoord, data[tcoord]);
            }
        }
    }

    function drawTimeline() {
        var line = createElement("line");
        line.setAttribute("x1", LINE_X);
        line.setAttribute("x2", LINE_X);
        line.setAttribute("y1", 0);
        line.setAttribute("y2", coordToY(START_YEAR));
        line.setAttribute("stroke", "#666");
        line.setAttribute("stroke-width", "1");
        svg.appendChild(line);

        var currYear = (new Date()).getUTCFullYear();
        for (var year = START_YEAR; year <= currYear; year++) {
            var mark = createElement("line");
            var yVal = coordToY(year);
            mark.setAttribute("x1", LINE_X-5);
            mark.setAttribute("x2", LINE_X+5);
            mark.setAttribute("y1", yVal);
            mark.setAttribute("y2", yVal);
            mark.setAttribute("stroke", "#666");
            mark.setAttribute("stroke-width", "1");
            svg.appendChild(mark);

            var text = createTextElement(year-0.02, year.toString());
            text.setAttribute("class", "year");
        }

        //top arrow
        var arrowL = createElement("line");
        arrowL.setAttribute("x1", LINE_X-4);
        arrowL.setAttribute("x2", LINE_X);
        arrowL.setAttribute("y1", 8);
        arrowL.setAttribute("y2", 0);
        arrowL.setAttribute("stroke", "#666");
        arrowL.setAttribute("stroke-width", "1");
        svg.appendChild(arrowL);

        var arrowR = createElement("line");
        arrowR.setAttribute("x1", LINE_X+4);
        arrowR.setAttribute("x2", LINE_X);
        arrowR.setAttribute("y1", 8);
        arrowR.setAttribute("y2", 0);
        arrowR.setAttribute("stroke", "#666");
        arrowR.setAttribute("stroke-width", "1");
        svg.appendChild(arrowR);
    }

    drawTimeline();

    for (var e in events) {
        createEvent(parseFloat(e), events[e]);
    }
});
