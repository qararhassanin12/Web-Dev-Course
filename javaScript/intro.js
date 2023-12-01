var message = "in global";
console.log("global message = " + message);


// inside a function 
var a = function () {
    var message = "inside a";
    console.log("a: message = " + message);
    b();
}

// out side function
function b() {
    console.log("b : message = " + message);
}
a();
