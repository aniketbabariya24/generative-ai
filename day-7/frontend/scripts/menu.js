function calculateTotalAmount() {
    let totalAmount = 0;
    cartItems.forEach(item => {
      totalAmount += item.price * item.quantity;
    });
    return totalAmount.toFixed(2);
  }

  let cartItems = [];

  const myId = localStorage.getItem('userId');

  fetch(`http://localhost:5000/customer/${myId}`)
    .then(response => response.json())
    .then(data => {
      cartItems = JSON.parse(data.cart);
      updateCartTable();
    });

  function updateCartTable() {
    const cartItemsContainer = document.getElementById('cart-items');
    cartItemsContainer.innerHTML = '';

    cartItems.forEach(item => {
        const existingItem = cartItems.find(item => item.id === item.id);
        if (existingItem) {
          existingItem.quantity += 0;
        } else {
          cartItems.push({ id: item .id, name: item  .name, price: item    .price, quantity: 1 })
        }
      const row = document.createElement('tr');

      const nameCell = document.createElement('td');
      nameCell.textContent = item.name;

      const priceCell = document.createElement('td');
      priceCell.textContent = `₹${item.price.toFixed(2)}`;

      const quantityCell = document.createElement('td');
      const quantityInput = document.createElement('input');
      quantityInput.type = 'number';
      quantityInput.value = item.quantity;
      quantityInput.min = 1;
      quantityInput.addEventListener('input', (event) => {
        const newQuantity = parseInt(event.target.value);
        item.quantity = newQuantity;
        updateCartTable();
      });
      quantityCell.appendChild(quantityInput);

      const totalCell = document.createElement('td');
      const total = item.price * item.quantity;
      totalCell.textContent = `₹${total.toFixed(2)}`;

      row.appendChild(nameCell);
      row.appendChild(priceCell);
      row.appendChild(quantityCell);
      row.appendChild(totalCell);

      cartItemsContainer.appendChild(row);
    });

    const totalAmountCell = document.createElement('td');
    totalAmountCell.setAttribute('colspan', '3');
    totalAmountCell.textContent = `Total Amount: ₹${calculateTotalAmount()}`;

    cartItemsContainer.appendChild(totalAmountCell);
  }

  fetch('http://localhost:5000/dishes')
    .then(response => response.json())
    .then(data => {
      const dishList = document.getElementById('dish-list');

      data.forEach(dish => {
        const card = document.createElement('div');
        card.className = 'card';

        const img = document.createElement('div');
        img.className = 'img';

        const dishImage = document.createElement('img');
        dishImage.src = dish.image;

        const desc = document.createElement('div');
        desc.className = 'desc';

        const all = document.createElement('div');
        all.className = 'all';

        const name = document.createElement('h3');
        name.textContent = dish.name;

        const description = document.createElement('p');
        description.textContent = dish.description;

        const price = document.createElement('p');
        price.textContent = `Price: ₹${dish.price}`;

        const addButton = document.createElement('button');
        addButton.textContent = 'Add';
        addButton.addEventListener('click', () => {
            dish.quantity++;
            const updatedDishData = {
                quantity:dish.quantity ,
              };
              
              // Make the fetch request to update the dish
              fetch(`http://localhost:5000/updatedish/${dish.id}`, {
                method: 'PUT',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(updatedDishData)
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
          fetch(`http://localhost:5000/addtocart/${myId}/${dish.id}`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
          })
            .then(response => response.json())
            .then(data => {
              if (data.message === 'Dish added to cart successfully') {
                const existingItem = cartItems.find(item => item.id === dish.id);
                if (existingItem) {
                  existingItem.quantity += 1;
                } else {
                  cartItems.push({ id: dish.id, name: dish.name, price: dish.price, quantity: 1 })
                }
                console.log(cartItems)
                updateCartTable();
            }
        })

    })
    img.appendChild(dishImage)
    all.appendChild(name);
    desc.appendChild(description);
    all.appendChild(price);
    all.appendChild(addButton);
    
    card.append(img, desc, all)
    
    dishList.appendChild(card);
})



    })