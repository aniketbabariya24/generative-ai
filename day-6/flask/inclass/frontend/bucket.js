document.addEventListener('DOMContentLoaded', function() {
    var bucketTable = document.getElementById('bucket-table');
    var tbody = bucketTable.querySelector('tbody');
  
    // Retrieve the bucket array from localStorage
    var bucket = JSON.parse(localStorage.getItem('bucket')) || [];
  
    // Populate the bucket table with the items
    bucket.forEach(function(item) {
      var row = document.createElement('tr');
      row.innerHTML = `
        <td>${item.name}</td>
        <td>${item.price}</td>
        <td>${item.description}</td>
      `;
      tbody.appendChild(row);
    });
  
    // Add event listener to the "Place Order" button
    var placeOrderButton = document.getElementById('place-order-button');
    placeOrderButton.addEventListener('click', function() {
      // Clear the bucket array in localStorage
      localStorage.removeItem('bucket');
  
      // Redirect to the order confirmation page
      window.location.href = 'confirmation.html';
    });
  });
  