
async function getRefuels(){
    const content_block = document.querySelector("#refuels_list");
    let content = "";
    const car_id = this.href
    console.log(car_id)
    await fetch("/api/refuel?car="+car_id, {
        method: 'POST',
        body: JSON.stringify() 
    })
    .then(response => response.json())
    .then(data => { 
        for (let key in data) {
            refuels = data[key];
            for (let k in refuels) {
                refuel = refuels[k];
                let paid = parseFloat(refuel.price) * parseFloat(refuel.amount);
                console.log(refuel.date)
                const date = new Date(refuel.date)
                content+=`
                <div class="col border car_col m-3">
                    <div id="car${refuel.id}">
                        <h2>${date.getDate()} ${date.getMonth()+1} ${date.getFullYear()}</h2>
                        <h4>Amount: ${refuel.amount}</h4>
                        <h4>Price: ${refuel.price}</h4>
                        <h4>Paid: ${paid}</h4>
                        <button class="del_btn" onclick = 'delRefuel(${refuel.id})'>DELETE</button>
                    </div>
                </div>`
            }
        }
    })
    .catch((error) => console.log(error))
    content_block.innerHTML = content;
};

function delRefuel(id){
    fetch("/delete-refuel", {
        method: "POST",
        body: JSON.stringify({ refuel_id: id }),
    }).then((_res) => {
        window.location.href = "/car/"+id;
    });
};

(() => {
    getRefuels();
})();