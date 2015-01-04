document.addEventListener("DOMContentLoaded", function(){
    setTimeout(function(){
        var nodes = document.querySelectorAll('.ellipsize');
        for (var i = 0; i < nodes.length; i++) {
            ellipsize(nodes[i]);
        }
    }, 50);
});

function ellipsize(node) {
    var lineHeight = parseInt(getComputedStyle(node).getPropertyValue("line-height"), 10);
    var numLines = parseInt(node.getAttribute("data-lines"), 10);
    console.log(lineHeight, numLines);
    for (var i = 0; i < 100; i++) {
        console.log(node.offsetHeight);
        if (node.offsetHeight <= lineHeight * numLines) {
            break;
        } else {
            //remove the last word
            console.log(node.innerText);
            node.innerText = node.innerText.replace(/\s\w*\W*\w*\W*$/, '');
        }
    }
}
