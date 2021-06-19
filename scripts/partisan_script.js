// Try to create bar graph using python DataFrame?

const date = new Date();
const [month, day, year] = [date.getMonth(), date.getDate(), date.getFullYear()];
const month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"];
const date_formatted = month_names[month] + " " + day + ", " + year

// Switch figure when clicked
let myFig = document.querySelector('figure');
let myImage = myFig.querySelector("img");
document.querySelector('figcaption').textContent =  "Partisan Podcast Leans on " + date_formatted;

// changes image when clicked
myImage.onclick = function() {
  let firstImageSrc = "/../podcast_day_data/podcast_leans_today.png";
  let mySrc = myImage.getAttribute('src');
  if(mySrc === firstImageSrc) {
    myImage.setAttribute('src', '/../podcast_day_data/temporal_leans_until_today.png');
    document.querySelector('figcaption').textContent =  "Partisan Podcast Across Time";
    document.getElementById("change_img").textContent = "Click the image to see " + date_formatted + "'s partisan leans.";
  }
  else {
    myImage.setAttribute('src', firstImageSrc);
    document.querySelector('figcaption').textContent =  "Partisan Podcast Leans on " + date_formatted;
    document.getElementById("change_img").textContent = "Click the image to see the partisan leans across time.";
  }
}
