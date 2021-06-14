let myImage = document.querySelector('img');

// changes image when clicked
myImage.onclick = function() {
  let firstImageSrc = '/images/may2021_ratings.png'
  let mySrc = myImage.getAttribute('src');
  if(mySrc === firstImageSrc) {
    myImage.setAttribute('src', '/images/yt_compare_new.png');
  }
  else {
    myImage.setAttribute('src', firstImageSrc);
  }
}

// Adds personalized message and stores inputted name
let headingMsg = 'Welcome, ';
let myHeading = document.querySelector('h1');
function setUserName() {
  let myName = prompt('Please enter your name: ');
  while(myName === null) {
    myName = prompt('Please enter your name: ');
  }
  localStorage.setItem('name', myName);
  myHeading.textContent = headingMsg + myName;
}
currName = localStorage.getItem('name');
if(!currName) {
  setUserName();
}
else {
  myHeading.textContent = headingMsg + currName;
}

// Sets new username when button is clicked
let myButton = document.querySelector('button');
myButton.onclick = function() {
  setUserName();
}
