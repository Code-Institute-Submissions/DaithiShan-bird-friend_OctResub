// check if on gallery page by searching for main gallery container
let galleryContainer = document.querySelector('.gallery-animate');

if(galleryContainer) {
  // if true, perform opacity animation on each child element
  let birdCards = galleryContainer.children;
  
  for (let i = 0; i < dogCards.length; i++){
    fadeIn(i, birdCards[i]);
  }
}