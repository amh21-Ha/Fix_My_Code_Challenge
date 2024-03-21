var dimension = 10;
var edge = '*';
var inside = ' ';
var printLine; // Corrected variable name

for (var i = 1; i <= dimension; i++) {
    if (i === 1 || i === dimension) {
        printLine = Array(dimension + 1).join(edge); // Corrected variable name
    } else {
        printLine = edge + Array(dimension - 1).join(inside) + edge; // Corrected variable name
    }
    console.log(printLine);
}
