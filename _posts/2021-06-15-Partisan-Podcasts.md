---
creator: Nick
---
After learning basic python (i.e., Numpy, Matplotlib, and Pandas) from [QuantEcon](https://quantecon.org), I wanted to create some projects of my own. Initially, I had planned to examine independent (alternative) media on YouTube, but that proved too difficult with the tools I had learned. Additionally, (and maybe more importantly), I realized it had already been done by [Pew](https://www.journalism.org/2020/09/28/a-closer-look-at-the-channels-producing-news-on-youtube-and-the-videos-themselves/). Still, the idea stuck with me.

So, I shifted my focus to podcasts. Podcast data are difficult to find; unlike YouTube, there are no fully-transparent statistics available for views, downloads, or revenue. Because I still wanted to focus on podcasts, I realized I needed to use other data as a proxy. Spotify and Apple podcasts, [two of the most popular podcast platforms](https://www.statista.com/statistics/943537/podcast-listening-apps-us/), both maintained a list of top news podcasts, which I obtained through [Chartable](https://chartable.com/charts/spotify/united-states-of-america-news-politics). This allowed me to extract the top 50 news and politics podcasts in America for any given day.

Using these data, I wanted to find both **1)** the impact of each podcast relative to each other and **2)** the number of podcasts per political leaning (simplified to left, center, and right, or neither if the podcast wasn't politically-based).

### 1) Analyzing Podcast Impact Using Google Trends

### 2) Finding Political Podcast Lean
Before I present these data nicely, I'll show my Jupyter Notebook, which details my somewhat messy thought process into how to go about classifying podcasts:

[Jupyter Notebook]({% link Partisan-Podcasts.html %}){:target="_blank"}

Currently, this code gets the current day's partisan podcast numbers. However, for meaningful analysis, these data would need to be collected over time. I was unable to find a source that kept track of each day's top 50 podcasts, so I decided to do so myself, using Hierarchical Data Format (HDF) to store each day's charts on my system.

Using Windows' Task Scheduler and the code I wrote, I will run this code everyday. Then, I will create another notebook to analyze the temporal data.

#### Task Scheduler
Thanks to [this](https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279), I made a batch file, then configured it to run using Task Scheduler at 3:00pm everyday. Originally, the file wouldn't run, but I unchecked the box [requiring AC power](https://superuser.com/questions/1149391/windows-10-scheduled-tasks-are-not-running), which fixed it. Additionally, I use a conda environment to run this code, so I put it in the batch file; however, you need to use ["call"](https://stackoverflow.com/questions/24678144/conda-environments-and-bat-files) to do this.

In a few months, I should have enough data to make the analysis more interesting. Right now, I configured the program to only save the charts, not my partisan lean assigments. This is because many of the podcasts in the top charts stay there and so it won't be a monumentous task to assign each podcast a partisan lean when all the daily data is combined into a dataframe.

#### Temporal Analyzer
Using code from my original notebook, I will create a dictionary (then load it in).
