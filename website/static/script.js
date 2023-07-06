function delCar(id){
    fetch("/delete-car", {
        method: "POST",
        body: JSON.stringify({ car_id: id }),
    }).then((_res) => {
        window.location.href = "/";
    });
};

async function getAllCars(){
    const content_block = document.querySelector(".cars");
    let content = "";

    await fetch("/api/cars", {
        method: 'POST',
        body: JSON.stringify() 
    })
    .then(response => response.json())
    .then(data => { 
        for (let key in data) {
            cars = data[key];
            for (let k in cars) {
                car = cars[k];
                content+=`
                <a href = "car/${car.id}">
                    <div class="car" id="car${car.id}">
                        <h1>${car.brand} ${car.model}</h1>
                        <h2>${car.current_odo}${car.units}</h2>
                        <button class="del_btn" onclick = 'delCar(${car.id})'>DELETE</button>
                    </div>
                </a>`
            }
        }
    })
    .catch((error) => console.log(error))
    content_block.innerHTML = content;
};

(() => {
    getAllCars();
})();