---
Creator: Nick
---
In the 2020 democratic presidential primary, there was an influx of candidates, with everyone claiming this election was the most important in their lifetimes and only they had the power to beat Donald Trump. Of the [29](https://en.wikipedia.org/wiki/2020_Democratic_Party_presidential_primaries) total candidates, 12 were running while currently serving in Congress (during the 116th session, which [ran from](https://www.senate.gov/legislative/DatesofSessionsofCongress.htm) January 3rd, 2019 to January 3rd 2021, excluding recesses). Of the [237 democrats in the House and 48 in the Senate](https://fas.org/sgp/crs/misc/R45583.pdf) (including independents who caucus with the democrats), around 4.2% were running for Congress. This is not an insignificant number, as candidates who have great levels of influence can possible cede ground to other party members/other parties during their time campaigning. This post is meant to analyze the Congressional actions of these 12 presidential candidates during their time running for the nomination. By comparing this period (and the 116th congress as a whole, when most candidates began their campaign) to other periods in Congress, we can attempt to understand the impact running for president has on congressional activity.

## A Look at the Data
Using the [ProPublica Congress API](https://projects.propublica.org/api-docs/congress-api/), I isolated the presidential candidates who were also in Congress and used different metrics to compare them as a group over time. Usually, I compare their presidential candidate selves to their past (and future) selves, as each of their habits are vastly different. The main question this post attempts to answer is thus: to what extent do members of congress running for president abdicate their congressional duties during their campaign? I attempt to use a variety of proxies, such as congressional statements, introduced bills, and various voting statistics to answer this question.

### Statements
Congressional statements, mainly in the form of press releases, are ways for congressmembers to communicate their opinions on bills or achievements to their constituents or to the broader public. These statements can get picked up by the media and potentially amplify someone's image. One may expect a presidential candidate in congress to write more press releases, so as to communicate their impact. However, candidates also may choose to focus on other avenues, such as social media or press releases through their presidential campaigns, instead of through congress. In my opinion, an increase of congressional statements doesn't necessarily correspond with an increase in congressional focus, but the opposite may be true. If one is using their congressional platform less, they are necessarily less focused on legislative issues, though they may be more attentive to the US political landscape as a whole.
![Presidential candidates total statements by month](\..\images\pres-candidates-graphs\statements_total_by_cand.png)

For almost all the candidates, the total number of congressional statements per month during their presidential campaigns was reasonably similar to during other periods. For a few candidates (Gabbard, Warren, Klobuchar, Delaney) there appeared to be a spike in congressional statements soon after their campaign announcements. For some (Gabbard, Sanders), statements have a generally downward trend. It appears there's nothing conclusive here; much of the monthly statement numbers fit with the rest of the non-campaign data.

**ADD LINE OF BEST FIT???**


### Bills
The main duty of congressmembers is (or in my opinion should be) to legislate. Introducing bills is a crucial part of a congressmember's job. During a presidential run, you may expect less attention to be paid to legislating and more to campaigning. However, not all presidential candidates have access to a congressional platform. Candidates could use their position to educate voters about meaningful legislation that corresponds with the message candidates want to send. Here, we examine the total bills introduced every month, again highlighting the duration of each candidate's presidential run.
![Presidential candidates total bills introduced by month](\..\images\pres-candidates-graphs\bills_introduced.png)

For many candidates (Klobuchar, Sanders, Gillibrand, Ryan, Delaney), the beginning of the campaign coincides with a spike in the total number of bills introduced per month. Though [many of these bills won't be passed](https://www.govtrack.us/congress/bills/statistics), they can generate attention, and congressmembers can blame the incumbent or opposing party when their grand, unreasonable bill dies in Congress. In one of the democratic debates, Sanders had a breakout moment where he tells a fellow candidate that he ["wrote the damn bill"](https://www.vox.com/policy-and-politics/2019/7/31/20748428/bernie-sanders-democratic-debate-wrote-damn-bill). These moments give congressmembers legitimacy; and though putting out bills right when the campaign starts may kill them legislatively, they could attract serious publicity. Of the new introduced bills, some (or many) of these bills may be serious, as passed legislation carries a power of its own; additionally, candidates may choose to focus on a handful of meaningful bills instead of pushing out as many as possible. Yet a congressmember can't realistically get their bill through committee and then the broader legislative body in a matter of months, especially when focusing on campaigning. By putting out a lot of bills with t, candidates can try to please everyone; they can say they're doing something, when in reality, it may have little chance of making a legislative impact.
<!-- single issue voters' exist, and are waiting for a candidate to address their issue. -->

### Votes
Voting is also a crucial duty of congressmembers. Therefore, I will be looking at aggregate voting statistics by congressional session (as I couldn't easily find these statistics by month).

First, missed votes are an important gauge of how focused a congressmember may be on their legislative duties. If they decide to spend a lot of time outside the chamber, it will correspond to missed votes. Here, I expect the presidential candidates to miss more votes during their campaign periods.
![Presidential candidates missed votes percent](\..\images\pres-candidates-graphs\missed_votes.png)

Wow... this seems the most consequential statistic yet. Congress 116 was a significant change for all of these presidential candidates in terms of missed votes. However, perhaps it was due to Covid-19, which intersected with the last year of this congressional session. To determine if this is the case, let's look at the average percent of missed votes for different groups in Congress)\*\*\*.
![Percent missed votes summary](\..\images\pres-candidates-graphs\missed_votes_summary.png))

Covid-19 doesn't seem to have had that large of an impact... The average missed votes percentage are similar for each session shown. Based on this graph, I think it's reasonable to conclude that the presidential candidates missed votes in session 116 at a significantly higher rate than regular congressmembers.

Another interesting statistic is the percent of votes for and against one's party. One may expect presidential candidates to vote more with their party during a presidential run as they try to please the voters in their entire party instead of in their specific congressional district or state. However, a candidate may also find success in voting against their party in an attempt to better differentiate themselves from other candidates, especially in a large field like the 2020 democratic primary. Because it's easier to visualize the percentage of votes against one's party than votes for one's party (as the percentages are smaller), I will display those.
![Presidential candidates votes against party percent](\..\images\pres-candidates-graphs\against_party_votes.png)

These results seem mixed; in session 116, some candidates appeared to take the former strategy, siding more/the same amount with other Democrats, while others increased their votes against their party. Let's again look at mean vote percentages to come to a better conclusion\*\*\*.
![Percent votes against party summary](\..\images\pres-candidates-graphs\against_party_summary.png)

It seems that the presidential candidates were more apt to vote against their party than other Democrats in Congress 115 and 116. A plausible explanation could be that the presidential candidates were the ones who developed the most individualism in the age of Trump. Perhaps the candidates didn't start voting more against their party because they planned to run but instead because they became more independent, believing their party was going in the wrong direction after Trump was elected.

*\*\*\* "Democrats" does not include Sanders*

### Statistical Analysis
Look at the statistics and see if they're significant.

## Campaign Finance Analysis
As it's known that you need money to succeed in politics, I'll look at the difference in fundraising for these canidates over time (both for congressional and presidential runs) and compare it with their success as a candidate.

Do higher fundraisers in Congress tend to make presidential runs? For this, we must look across time at many presidential elections. However, for now, we will retain our focus on 2020.

## Recap
Perhaps in the future, I could analyze the total number of statements or bills introduced based on important congressional election dates.

<!-- TODO: Get total contributions for a congressional election cycle
i.e. 2 yrs for the house and 6 yrs for the senate (total),
then compare with presidential fundraising. For the latter step,
find out what everything in FEC df means, e.g. net operating expenditures, etc.

use PEW or GALLUP! research, research, research

also, ask how often in debates do candidates mention their bills? somehow research this?

grammar -- congressmember? two words? capitalized? also, "I" vs. "We"-->
