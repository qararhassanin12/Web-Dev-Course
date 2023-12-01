// should be undefined
var x;
console.log(x);

if(x == undefined) {
    console.log(" x is undefined");
}

// if it have value, it will be defined otherthan undefined
x = 5;
if (x == undefined) {
    console.log(" x is undefined");
}
else {
    console.log(" x has been defined");
}