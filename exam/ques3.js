// using ajax
const getData = () => {
    const xhr = new XMLHttpRequest()
    xhr.open('GET', "https://fakestoreapi.com/products/", true)
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            const products = JSON.parse(this.responseText)
            let html = `<table border = 1>
            <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Description</th>
                <th>Category</th>
                <th>Image</th>
                <th>Rating</th>
                <th>Price</th>
            </tr>`
            products.forEach(element => {
                html += `<tr><td>${element.id}</td>`
                html += `<td>${element.title}</td>`
                html += `<td>${element.description}</td>`
                html += `<td>${element.category}</td>`
                html += `<td><img src = "${element.image}" width=50
height=50></td>`
                html += `<td>${element.rating.rate}</td>`
                html += `<td>${element.price}</td></tr>`
            })
            html += "</table>"
            const holder = document.getElementsByTagName("body")
            holder[0].innerHTML = html
        }
    }
    xhr.send()
}
getData()