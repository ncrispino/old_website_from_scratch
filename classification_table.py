######################################################
# Self-rating
######################################################
import pickle
import numpy as np
import pandas as pd

with open('podcast_day_data/partisan_database.pkl', 'rb') as f:
    partisan_database = pickle.load(f)

# lists known companies and/or names and their ratings--either Left, Right, or Center
# some need to be hard-coded in as they are very difficult to find
# need to alert myself--if there's new podcast on charts that isn't classified--in some way
# classifications written as a nested list consisting of many [podcast name/source, justification, link to reason] in a list as
# the first item (index 0) of the outside list and the political justification as the second item (index 1) of the that list
names_classify = []
right_names = [[["The Realignment", "Hosts Saagar Enjeti and Marshall Kosloff both describe themselves as right-of-center; \
though they (at least Saagar) may be more populist, they still hold views better aligned with conservatives", ""],
                ["Dan Bongino", "Ran for Congress as republican", "https://en.wikipedia.org/wiki/Dan_Bongino"],
                ["Mark Levin", "Fox News contributor and worked in Reagan White House", "https://en.wikipedia.org/wiki/Mark_Levin"],
                ["Fearless with Jason Whitlock", "From The Blaze", "https://en.wikipedia.org/wiki/Blaze_Media"],
                ["Office Hours with Georgia Howe", "From The Daily Wire", "https://en.wikipedia.org/wiki/The_Daily_Wire"],
                ["Part Of The Problem", "Hosted by self-described libertarian", "https://gasdigitalnetwork.com/gdn-show-channels/part-of-the-problem/"],
                ["Soundfront", "From Abbson, a conservative media company", "https://soundfront.com/"],
                ["Hodgetwins", "Self-proclaimed conservatives", "https://en.wikipedia.org/wiki/Hodgetwins"],
                ["The Rush Limbaugh Show", "Conservative talk radio show", "https://en.wikipedia.org/wiki/The_Rush_Limbaugh_Show"],
                ["The Clay Travis and Buck Sexton Show", "Conservative talk radio show taking over for The Rush Limbaugh Show", "https://en.wikipedia.org/wiki/The_Rush_Limbaugh_Show"]],
               "Right"]
left_names = [[["Crooked Media", "Created by former Obama staffers", "https://en.wikipedia.org/wiki/Crooked_Media"],
               ["Real Time with Bill Maher",
                "Bill Maher is self-described leftist; against cancel-culture but still a progressive",
                "https://en.wikipedia.org/wiki/Bill_Maher#Politics"],
               ["Chapo Trap House", "Self-described far-left", "https://en.wikipedia.org/wiki/Chapo_Trap_House"],
               ["QAnon Anonymous", "Explores right-wing QAnon theory; will inherently have leftist lean", ""],
               ["Krystal Kyle & Friends", "Hosts Krystal Ball and Kyle Kulinski are self-described progressives", ""],
               ["Fear & Malding", "Self-described as left-leaning podcast", "https://open.spotify.com/show/5uKAwUEZun3X9NyxnwfS7e (Fear & Malding)"],
               ["Q Clearance: The Hunt for QAnon", "Explores right-wing QAnon theory; will inherently have leftist lean", ""],
               ["The Majority Report with Sam Seder", "Promotes left-wing politics", "https://en.wikipedia.org/wiki/The_Majority_Report_with_Sam_Seder"]],
              "Left"]
center_names = [[["Breaking Points with Krystal and Saagar", "Hosts Krystal Ball and Saagar Enjeti both populists \
but the former leans left and the latter leans right. Even though they aren't the center, contains representative from \
both and doesn't fit well on either side. See info about their old show, Rising, for more.",
                 "https://en.wikipedia.org/wiki/Rising_(news_show)"],
                  ["Devil May Care Media", "Founder Megyn Kelly is self-described independent",
                   "https://en.wikipedia.org/wiki/Megyn_Kelly"],
                  ["Axios & Pushkin Industries", "Most readers moderate, slightly left-leaning but not entirely",
                   "https://en.wikipedia.org/wiki/Axios_(website)"],
                   ["Mea Culpa with Michael Cohen", "Hosted by Trump's former lawyer, which would indicate a right lean. \
                   However, he has begun to criticize Trump, which would align him better with the left. As such, I'll place him as center.",
                   "https://en.wikipedia.org/wiki/Michael_Cohen_(lawyer)"]],
                 "Center"]
names_classify.extend([right_names, left_names, center_names])

all_classify = []
# names_classify has 3 lists inside, one for each classification, of the structure described above
for nc in names_classify:
    for name_just in nc[0]:
        if name_just[2] != "": name_just[2] = ("<a href=\"" + name_just[2] + "\">Link</a>")
        partisan_database[name_just[0]] = nc[1]
        name_just.append(nc[1])
        all_classify.append(name_just)

# all_classify is a nested list of [podcast name/source, justification, classification]
cols = ["Name/Source", "Justification", "Reason for Justification", "Partisan Lean"]
df = pd.DataFrame(all_classify, columns=cols)
# df.to_html("classify_justify")

with open('podcast_day_data/partisan_database.pkl', 'wb') as f:
    pickle.dump(partisan_database, f)

with open('podcast_day_data/source_list.pkl', 'rb') as f:
    source_list = pickle.load(f)

# Get all names/sources not self-defined
keys = set(partisan_database.keys()).difference(set(df["Name/Source"]))
given_rank_df = (
                    pd.DataFrame([keys, ["AllSides" for i in range(len(keys))], [source_list[k] for k in keys],
                    [partisan_database[k] for k in keys]])
                    .T
                    .rename(columns=dict(enumerate(cols)))
                )
final_classify_df = pd.concat([df, given_rank_df]).reset_index(drop=True).sort_values("Name/Source")
final_classify_df.to_html("podcast_day_data/classify_justify", index=False, escape=False, render_links=True)
