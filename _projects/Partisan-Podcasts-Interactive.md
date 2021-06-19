---
title: Partisan Podcasts Interactive
---
<div class="change_img">Click the image to see the partisan leans across time.</div>

<figure>
  <img src="\..\podcast_day_data\podcast_leans_today.png" alt="Current day's partisan leans">
  <figcaption>Partisan Podcast Leans Today</figcaption>
</figure>

Partisan Database (with justifications):
  put a search bar here and list classifications in table:

  \
  \
  \
  \
***put below in partisan podcast post, not project????***

For this, I created another batch file, this time with the contents of the updated Jupyter Notebook, and set it to run after the webscraping batch file.

From this, I got each day's current bar graph and graph over time (which are deleted the next time it is run, replaced by the new graphs). These can then be easily displayed in the website.

However, though the images are automatically updated, the webpage isn't. This is due to the Python files running and storing the data locally. Ideally, these scripts should be run on the cloud and the webpage should fetch the data (including graphs) from the the cloud to be put on the webpage.

This would require a lot of work--as I could no longer use jekyll, which is made for static sites. Because my focus isn't in web-development but in economics/politics and data analysis, I'm going to focus on doing further analysis rather than creating a more interactive user experience. Perhaps in the future I could return to this using a web-framework like django. However, my interests lie elsewhere, so for now, this must do.

<script src="..\scripts\partisan_script.js"></script>
