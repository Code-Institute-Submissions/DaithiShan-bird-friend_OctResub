// check if on gallery page by searching for main gallery container
let galleryContainer = document.querySelector('.gallery-animate');

if(galleryContainer) {
  // if true, perform opacity animation on each child element
  let birdCards = galleryContainer.children;
  
  for (let i = 0; i < birdCards.length; i++){
    fadeIn(i, birdCards[i]);
  }
}

// Function for adding a delay within a loop
// Souce: https://www.geeksforgeeks.org/how-to-add-a-delay-in-a-javascript-loop/
function fadeIn(idx, e){
  setTimeout(function() {
    e.classList.remove('opacity-0');
  }, 500 + (250 * idx));
}