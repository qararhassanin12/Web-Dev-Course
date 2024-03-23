const products = [
    {
        "count": 7,
        "items": ["socks", "pants", "shirts", "hats"], 
        "manufacturer": {
            "name": "Molly's Seamstress Shop", 
            "id": 23424,
            "location": {
                "address": "123 Pickleton Dr.",
                "city": "Tueson",
                "state": "AZ",
                "zip": 85705
            }
        },
        "total_price": "$342.4", 
        "purchase_date": "2023-12-19", 
        "country": "USA"
    }, 
    {
        "count": 43,
        "items": ["socks", "pants", "shirts", "hats"], 
        "manufacturer": {
            "name": "BV Seamselss Shop",
            "id": 23424,
            "location": {
                "address": "1233 Pickleton Dr.", 
                "city": "Tueson",
                "state": "AZ",
                "zip": 85705
            }
        },
        "total_price": "$542.4", 
        "purchase_date": "2023-12-19", 
        "country": "China"
    } 
    
]

// part 1
let res = products.filter(element => {
    return element.count <= 50 && element.count >= 40
})
console.log(res)


// part 2
products.forEach(element => {
    console.log(`Name: ${element.manufacturer.name} \nAddress:
${element.manufacturer.location.address}`)
})


// part 3
products.forEach(element => {
    console.log(`Total Records: ${element.items.length}`)
})


// part 4
products.map(element => {
    element.total_price + 5
})


// part 5
products.forEach(element => {
    if (element.manufacturer.location.zip >= 33445 &&
        element.manufacturer.location.zip <= 85705) {
            console.log(element)
    }
})


// part 6
totalPrice = 0 
products.forEach(element => {
    totalPrice += element.total_price
})
products.forEach(element => {
    if (element.total_price > (totalPrice / products.length)) {
        console.log(element)
    }
})


// part 7
totalPrice = 0
products.forEach(element => {
    totalPrice += element.total_price
}) 
console.log(totalPrice)


// part 8
const startDate = new Date("2002-05-30")
const endDate = new Date("2025-06-30")

const result = products.filter(element => {
    const currentDate = new Date(element.purchase_date) 
    return currentDate >= startDate && currentDate <= endDate
})
console.log(result)


// part 9
let s = [] 
products.forEach(element => {
    s.push(element.country)
})
console.log(new Set(s))


// part 10
products.forEach(element => {
    console.log(`Country: ${element.country}\nName:
${element.manufacturer.name}\nID: ${element.manufacturer.id}`)
})