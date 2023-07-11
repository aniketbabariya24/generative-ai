
fetch("http://localhost:5000/customers")
.then(response => response.json())
.then(data => {
   append(data)
})
.catch(error => {
    console.log(error);
    alert("Failed to fetch customers");
});


const customerList = document.getElementById("customer-list");

let append=(myData)=>{
    customerList.innerHTML=null
myData.forEach(customer => {
    const row = document.createElement("tr");

    const nameCell = document.createElement("td");
    nameCell.textContent = customer.name;

    const emailCell = document.createElement("td");
    emailCell.textContent = customer.email;

    const cityCell = document.createElement("td");
    cityCell.textContent = customer.city;
    const deleteCell = document.createElement("td");
    deleteCell.className="dCell"
    const btn= document.createElement("button")
    btn.className="deleteBtn"
    btn.textContent = "Delete"
    
   btn.onclick=()=>deleteIteam(customer.id)
    deleteCell.append(btn)
    row.appendChild(nameCell);
    row.appendChild(emailCell);
    row.appendChild(cityCell);
    row.appendChild(deleteCell);

    customerList.appendChild(row);
});

}



function deleteIteam(did){
    fetch(`http://localhost:5000/deletec/${did}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
        // body: JSON.stringify(updatedDishData)
      })
        .then(response => response.json())
        .then(data => {
          console.log(data); // Log the response from the server
          // Handle the response as needed
        })
        .catch(error => {
          console.log(error); // Log any errors
          // Handle errors as needed
        })
    window.alert("Are you sure")
        
        fetch("http://localhost:5000/customers")
.then(response => response.json())
.then(data => {
   append(data)
})
.catch(error => {
    console.log(error);
    alert("Failed to fetch customers");
});

}