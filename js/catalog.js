
async function loadProducts() {
    let request = new XMLHttpRequest();
    request.open("GET", 'http://127.0.0.1:8000/PEI/getProd/', true);
    request.send();
    request.onload = () => {
        if (request.status == 200) {
            console.log(JSON.parse(request.response)['data']);
            let products = JSON.parse(request.response)['data'];

            var section = document.getElementsByClassName("products")[0]
            var list = section.getElementsByClassName("list")[0]

            for (const product of products) {
                let article = document.createElement("article");
                article.classList.add("product");
                list.appendChild(article);

                let productInner = document.createElement("div");
                productInner.classList.add("product-inner");
                article.appendChild(productInner);

                let link = document.createElement("a");
                link.classList.add("image");
                link.href = "single.html?id="+product['id'];
                productInner.appendChild(link);

                let image = document.createElement("img");
                image.src = 'http://127.0.0.1:8000/' + product['image'];
                image.alt = "Braucamais";
                link.appendChild(image);

                let button = document.createElement("span");
                button.classList.add("view");
                button.innerHTML = "View";
                link.appendChild(button);

                let description = document.createElement("div");
                description.classList.add("descr");
                productInner.appendChild(description);

                let name = document.createElement("h2");
                name.classList.add("name");
                name.innerHTML = product['model'];
                description.appendChild(name);

                let price = document.createElement("p");
                price.classList.add("price");
                price.innerHTML = product['price']+'$';
                description.appendChild(price);
            }
        }

    }
}
