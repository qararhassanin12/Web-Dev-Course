// Define an array of names
var names = ["John", "Jane", "Jim", "Jack"];

// Loop over the array of names
for (var i = 0; i < names.length; i++) {
    // Get the current name
    var name = names[i];

    // Determine whether to say hello or goodbye based on the first letter of the name
    if (name.charAt(0).toLowerCase() === 'j') {
        // Print goodbye for names starting with 'j' or 'J'
        console.log("Goodbye " + name);
    } else {
        // Print hello for names starting with any other letter
        console.log("Hello " + name);
    }
}
