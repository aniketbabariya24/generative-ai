fetch("http://localhost:5000/dishes")
    .then(response => response.json())
    .then(data => {
        appendDishes(data);
    })
    .catch(error => {
        console.log(error);
        alert("Failed to fetch dishes");
    });

const dishesList = document.getElementById("dishes-list");

function appendDishes(data) {
    data.forEach(dish => {
        const row = document.createElement("tr");

        const nameCell = document.createElement("td");
        nameCell.textContent = dish.name;

        const priceCell = document.createElement("td");
        priceCell.textContent = dish.price;

        const actionsCell = document.createElement("td");
        actionsCell.className = "actions";
        
        const editButton = document.createElement("button");
        editButton.textContent = "Edit";
        
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        
        actionsCell.appendChild(editButton);
        actionsCell.appendChild(deleteButton);
        
        row.appendChild(nameCell);
        row.appendChild(priceCell);
        row.appendChild(actionsCell);

        dishesList.appendChild(row);
    });
}
