function delCar(id){
    fetch("/delete-car", {
        method: "POST",
        body: JSON.stringify({ car_id: id }),
    }).then((_res) => {
        window.location.href = "/";
    });
}