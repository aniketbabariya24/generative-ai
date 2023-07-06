// Image Carousel functionality
const cartData = '[{\"_id\": {\"$oid\": \"64a4f2190eac2c662e07dd09\"}, \"name\": \"Biryani\", \"description\": \"Very good biryani\", \"price\": 200.0, \"stocks\": 35, \"isAvailable\": true}, {\"_id\": {\"$oid\": \"64a4f2880eac2c662e07dd0a\"}, \"name\": \"Samosa\", \"description\": \"Very good Samosa\", \"price\": 20.0, \"stocks\": 57, \"isAvailable\": true}]';

const cartItems = JSON.parse(cartData);

for (const item of cartItems) {
  const price = item.price;
  console.log(price);
}

let currentImageIndex = 0;
const carouselImages = document.querySelectorAll('.carousel img');

function changeImage() {
  carouselImages[currentImageIndex].classList.remove('active');
  currentImageIndex = (currentImageIndex + 1) % carouselImages.length;
  carouselImages[currentImageIndex].classList.add('active');
}

setInterval(changeImage, 2000);
