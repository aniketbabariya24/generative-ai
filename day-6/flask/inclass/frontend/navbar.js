
var addAmountPopup = document.getElementById("addAmountPopup");
var addAmountForm = document.getElementById("addAmountForm");
var addAmountBtn = document.getElementById("addAmountBtn");
var walletAmount = document.getElementById("walletAmount");

addAmountBtn.addEventListener("click", function(event) {
    event.preventDefault();
    addAmountPopup.style.display = "block";
});

addAmountForm.addEventListener("submit", function(event) {
    event.preventDefault();

    var amount = document.getElementById("amount").value;
    var id= localStorage.getItem("userId")

    // Send POST request to updatewallet endpoint
    fetch(`http://localhost:5000/updatewallet/${id}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ amount: +amount })
    })
    .then(function(response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error("Error: " + response.status);
        }
    })
    .then(function(data) {
        console.log(data)
        // Update wallet amount in the navbar
        walletAmount.innerText = "Wallet: ₹" + data.wallet;

        // Close the popup
        addAmountPopup.style.display = "none";

        // Reset the form
        addAmountForm.reset();

        // Show success message
        alert("Amount added to wallet successfully");
    })
    .catch(function(error) {
        console.log(error);
        alert("Error adding amount to wallet");
    });
});

