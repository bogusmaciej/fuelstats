function delCar(id){
    fetch("/delete-car", {
        method: "POST",
        body: JSON.stringify({ car_id: id }),
    }).then((_res) => {
        window.location.href = "/";
    });
}

function getCars(){
    return fetch("/api/cars")
    .then(response => response.json())
    .catch((error) => console.log(error))
};