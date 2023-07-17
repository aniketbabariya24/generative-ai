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

        const editCell = document.createElement("td");
        editCell.className = "edit";
        const deleteCell = document.createElement("td");
        deleteCell.className = "delete";
        
        const editButton = document.createElement("button");
        editButton.textContent = "Edit";
        
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        
        editCell.appendChild(editButton);
        deleteCell.appendChild(deleteButton);
        
        row.appendChild(nameCell);
        row.appendChild(priceCell);
        row.appendChild(editCell);
        row.appendChild(deleteCell);

        dishesList.appendChild(row);
    });
}
