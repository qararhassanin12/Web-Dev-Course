// Better way: object literal
var facebook = {
    name: "Facebook",
    ceo: {
        firstName: "Mark",
        favColor: "blue"
    },
   // $stock: 110
   "stock of company ": 110
};
var company = {
    name: "Instagram",
    ceo: {
        firstName: "Sano",
        favColor: "red"
    },
    "stock of company ": 112
};
console.log(facebook);
console.log(company);
console.log(facebook.ceo.firstName);
console.log(company.ceo);
