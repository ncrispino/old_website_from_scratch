---
Creator: Nick
---
In the 2020 democratic presidential primary, there was an influx of candidates, with everyone claiming this election was the most important in their lifetimes and only they had the power to beat Donald Trump. Of the [29](https://en.wikipedia.org/wiki/2020_Democratic_Party_presidential_primaries) total candidates, 12 were running while currently serving in Congress (during the 116th session, which [ran from](https://www.senate.gov/legislative/DatesofSessionsofCongress.htm) January 3rd, 2019 to January 3rd 2021, excluding recesses). Of the [237 democrats in the House and 48 in the Senate](https://fas.org/sgp/crs/misc/R45583.pdf) (including independents who caucus with the democrats), around 4.2% were running for Congress. This is not an insignificant number, as candidates who have great levels of influence can possible cede ground to other party members/other parties during their time campaigning. This post is meant to analyze the Congressional actions of these 12 presidential candidates during their time running for the nomination. By comparing this period (and the 116th congress as a whole, when most candidates began their campaign) to other periods in Congress, we can attempt to understand the impact running for president has on congressional activity.

## A Look at the Data
Using the [ProPublica Congress API](https://projects.propublica.org/api-docs/congress-api/), I isolated the presidential candidates who were also in Congress and used different metrics to compare them as a group over time. Usually, I compare their presidential candidate selves to their past (and future) selves, as each of their habits are vastly different.

### Statements
Congressional statements, mainly in the form of press releases, are ways for congresspeople to communicate their opinions on bills or achievements to their constituents. These statements can get picked up by the media and potentially boost someone's image. ***research more***.
![Presidential candidates total statements by month](\..\images\pres-candidates-graphs\statements_seasons_by_cand.png)

### Bills
The main duty of congressmembers is (or should be) to legislate. Introducing bills is a crucial part of a congressmember's job. During a presidential run, you would expect less attention to be paid to legislating and more to campaigning. However, part of campaining could be introducing meaningful legislation that corresponds with the message candidates want to send to voters. Here, we examine the total bills introduced every month, again highlighting the time during presidential runs.
![Presidential candidates total bills introduced by month](\..\images\pres-candidates-graphs\bills_introduced.png)

### Votes
Voting is also a crucial duty of congressmembers. Therefore, I will be looking at some aggregate voting statistics per congressional session (as I couldn't easily find these statistics by month).

First, missed votes are an important gauge of how focused a congressmember may be on their legislative duties. If they decide to spend a lot of time outside the chamber, it will correspond to missed votes. Here, we expect the presidential candidates to miss more votes during their campaign periods.
![Presidential candidates missed votes percent](\..\images\pres-candidates-graphs\missed_votes.png)

Wow! Congress 116 was a pretty significant change for all of these presidential candidates in terms of missed votes. However, perhaps it was due to Covid-19, which intersected with the last year of this congressional session. To determine if this is the case, let's look at the average percent of missed votes for different groups in Congress.
![Percent missed votes summary](\..\images\pres-candidates-graphs\missed_votes_summary.png)

Covid-19 doesn't seem to have had that large of an impact... Based on this graph, I think it's reasonable to conclude that the candidates missed votes at a much, much higher rate than regular congressmembers.

Another interesting statistic is the percent of votes for and against one's party. One may expect presidential candidates to vote more with the party during a presidential run as they try to please their entire party's voter base instead of their specific congressional district. However, a candidate may also find success in voting more against their party in an attempt to better differentiate themselves. Because it's easier to visualize the percent of votes against party (as the percentages are smaller), I will display those.
![Presidential candidates votes against party percent](\..\images\pres-candidates-graphs\against_party_votes.png)

These results seem mixed; some candidates appeared to take the former strategy, siding more/the same amount with other Democrats, while others increased their votes against their party. Let's again look at mean votes across different categories to come to a better conclusion.
![Percent votes against party summary](\..\images\pres-candidates-graphs\against_party_summary.png)

It seems that the presidential candidates were more apt to vote against their party than other Democrats in Congress 115 and 116. From this, it seems that the presidential candidates were the ones who developed the most individualism in the age of Trump. Perhaps the candidates didn't start voting against their party because they planned to run but instead because they self-selected, believing their party was going in the wrong direction after Trump was elected.

### Statistical Analysis
Look at the statistics and see if they're significant.

## Campaign Finance Analysis
As it's known that you need money to succeed in politics, I'll look at the difference in fundraising for these canidates over time (both for congressional and presidential runs) and compare it with their success as a candidate.

Do higher fundraisers in Congress tend to make presidential runs? For this, we must look across time at many presidential elections. However, for now, we will retain our focus on 2020.

<!-- TODO: Get total contributions for a congressional election cycle
i.e. 2 yrs for the house and 6 yrs for the senate (total),
then compare with presidential fundraising. For the latter step,
find out what everything in FEC df means, e.g. net operating expenditures, etc. -->
