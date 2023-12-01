// Default values

function orderChickenWith (sideDish) {
    //if (sideDish === undefined) {
      //  sideDish = "whatever!";
    //}
    sideDish = sideDish || "whatever!";
    console.log("Chicken with " + sideDish);
}
orderChickenWith("noodles");
orderChickenWith();


// object creation

var company = new Object();
company.name = "Facebook";
company.ceo = new Object ();
company.ceo.firstname = "Mark";
company.ceo.favColor = "blue";

console.log(company);
console.log("Company CEO name is : " + company.ceo.firstname);
console.log(company["name"]);
company.$stock = 110;
console.log(company);