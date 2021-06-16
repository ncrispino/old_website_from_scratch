---
creator: Nick
---
After learning basic python (i.e., Numpy, Matplotlib, and Pandas) from [QuantEcon](https://quantecon.org), I wanted to create some projects of my own. Initially, I had planned to examine independent (alternative) media on YouTube, but that proved too difficult with the tools I had learned. Additionally, (and maybe more importantly), I realized it had already been done by [Pew](https://www.journalism.org/2020/09/28/a-closer-look-at-the-channels-producing-news-on-youtube-and-the-videos-themselves/). Still, the idea stuck with me.

So, I shifted my focus to podcasts. Podcast data are difficult to find; unlike YouTube, there are no fully-transparent statistics available for views, downloads, or revenue. Because I still wanted to focus on podcasts, I realized I needed to use other data as a proxy. Spotify and Apple podcasts, [two of the most popular podcast platforms](https://www.statista.com/statistics/943537/podcast-listening-apps-us/), both maintained a list of top news podcasts, which I obtained through [chartable.com](https://chartable.com/charts/spotify/united-states-of-america-news-politics). This allowed me to extract the top 50 news and politics podcasts in America for any given day.

Using these data, I wanted to find both **1)** the impact of each podcast relative to each other and **2)** the number of podcasts per political leaning (simplified to left, center, and right, or neither if the podcast wasn't politically-based).

### 1) Analyzing Podcast Impact Using Google Trends

### 2) Finding Political Podcast Lean
Before I present these data nicely, I'll show my Jupyter Notebook, which details my somewhat messy thought process in how to go about classifying podcasts

<!-- INCLUDE JUPYTER NOTEBOOK HERE!!! -->

Currently, this code gets the current day's partisan podcast numbers. However, for meaningful analysis, these data would need to be collected over time. I was unable to find a source that kept track of each day's top 50 podcasts, so I decided to do so myself.
