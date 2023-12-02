// Function explained...
// Function are first-class data
// Function are objects

function multiply(x, y) {
    return x * y;
}
console.log(multiply(5, 3));
multiply.version = "v.1.0.0";
console.log(multiply.version);


// Function factory
function makeMultiplier(multiplier) {
    var myFunc = function (x) {
        return multiplier * x;
    };

    return myFunc;
}

var multiplyBy3 = makeMultiplier(3);
console.log(multiplyBy3(10));
var doubleAll = makeMultiplier(2);
console.log(doubleAll(100));
// passing function as arguments
function doOperation(x, operation) {
    return operation(x);
}

var result = doOperation(5, multiplyBy3);
console.log(result);
result = doOperation(100, doubleAll);
console.log(result);
