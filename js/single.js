async function loadProduct(){
    let info = window.location.search;
    let id = info.charAt(info.length-1);
    let request = new XMLHttpRequest();
    request.open("GET", 'http://127.0.0.1:8000/PEI/getProd/' + id, true);
    request.send();
    request.onload = () => {
        if (request.status == 200) {
            let item = JSON.parse(request.response)['data'][0];

            let image = document.getElementById("attels");
            image.src = 'http://127.0.0.1:8000/' + item['image'];

            let Title = document.getElementById("nosaukumsUnCena");
            Title.innerHTML = item['model']+'<br>'+item['price']+'$';

            let brand = document.getElementById("firma");
            brand.innerHTML = item['brand'];

            let name = document.getElementById("nosaukums");
            name.innerHTML = item['model'];
        }
    }
}