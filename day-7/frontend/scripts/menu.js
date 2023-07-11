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
    totalAmountCell.className="ta"
    totalAmountCell.setAttribute('colspan', '4');
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


        const all = document.createElement('div');
        all.className = 'all';

        const name = document.createElement('h3');
        name.textContent = dish.name;
        const desc = document.createElement('p');
        desc.className="desc"
        desc.textContent = dish.description;

        const price = document.createElement('p');
        price.className="ppp"
        price.textContent="The Special Price: "
        const sp= document.createElement("span")
        sp.textContent = `₹${dish.price}`;
         price.append(sp)
        const addButton = document.createElement('button');
        addButton.textContent = 'Add to Order';
        addButton.addEventListener('click', () => {
          addButton.disabled=true
          addButton.style.backgroundColor="grey"
          addButton.style.color="white"
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
    all.appendChild(desc);
    all.appendChild(price);
    all.appendChild(addButton);
    
    card.append(img,  all)
    
    dishList.appendChild(card);
})



    })

    console.log(cartItems.length)
    let text= document.createElement("h1")
    text.textContent="Nothing";
    const cartItemsContainer = document.getElementById('cart-items');
    
   
    