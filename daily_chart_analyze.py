######################################################
# Setup
######################################################

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import time
from datetime import date
end_date = pd.to_datetime(date.today()) # to adjust end date
today_date_short = end_date.strftime('%b%d%y')

# turn on latex for matplotlib
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=r"\usepackage{amsmath}"

######################################################
# Definitions
######################################################

# Useful functions/definitions
def remove_spines(ax, sides=["top", "right"]):
    """
    Removes spines from all graphs in given axis. Works with an individual axis or list of axes.
    By default removes top and right spines. Returns ax.
    """
    for side in sides:
        try:
            for a in ax:
                a.spines[side].set_visible(False)
        except:
            ax.spines[side].set_visible(False)
    return ax
facecolor=(245/255, 245/255, 245/255)

# Clean Media
def clean_names(names):
    """
    Removes filler words from name list so allsides can easily search.
    Returns altered list.
    """
    # deep copy
    name_list = [n for n in names]
    # remove filler words from source list so allsides can easily search
    abbrev_re = re.compile(r"([A-Z]{2,})")
    for i in range(len(name_list)):
        # remove 'podcasts', 'networks', 'the' from name
        name_list[i] = re.sub(r"[Pp]odcasts?|[Nn]etworks?|\s?[Tt]he\s?|[Oo]pinion|\s[Rr]adio$", "", name_list[i])
        # if there's an abbreviation in all caps (more than two capital letters next to each other,
        # replace name str with abbreviation
        abbrev = re.findall(abbrev_re, name_list[i])
        if len(abbrev) > 0:
            name_list[i] = abbrev[0]
        name_list[i] = name_list[i].strip()
    return name_list

def find_biases_dict(source_list, partisan_leans):
    """
    Takes a list of strings and finds their corresponding partisan lean according to allsides.com
    and/or the dictionary provided.
    If there is no partisan lean, the value is not placed in the dictionary.
    Adds to given dictionary with the keys as the source names and the values as the partisan leans.
    Returns dataframe with source names and links to AllSides searches.
    """
    source_links = dict()
    source_list_use = clean_names(source_list)
    options = Options()
    options.add_argument("--headless")
    ua = UserAgent().random
    options.add_argument(f"user-agent={ua}")
    driver = webdriver.Chrome("C:/Users/ncris/econ/chromedriver_win32/chromedriver.exe", options=options)
    ratings_url = "https://www.allsides.com/media-bias/media-bias-ratings"
    driver.get(ratings_url)
    for source, source_full in zip(source_list_use, source_list):
        # if source not already in dict
        if partisan_leans.get(source_full) == None:
            # wait before next round
            time.sleep(0.1)
            # find input and type source
            # Waits 10 seconds until element with id "edit-title" is clickable -- if it's not or time passes, throws error
            input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "edit-title")))
    #         input_element = driver.find_element_by_id("edit-title")
            input_element.clear()
            input_element.send_keys(source, Keys.RETURN)
            ratings_soup = BeautifulSoup(driver.page_source, "lxml")
            try:
                ratings_table = ratings_soup.find("table", {"class", "views-table cols-4"})
                source_name = ratings_table.find("td", {"class", "views-field views-field-title source-title"}).text
                rating = ratings_table.find("td", {"class", "views-field views-field-field-bias-image"}).find("img").get("title").strip()
                # Only use Center; consider mixed as center, as it is not overly partisan
                if rating == "Mixed":
                    rating = "Center"
                # add last word of AllSides rating to dict, which is of form AllSides Media Bias Rating: _____ (or lean _____)
                # keys of dict are full names of source, not cleaned names
                partisan_leans[source_full] = rating.split(" ")[-1]
                source_links[source_full] = "<a href=\"" + driver.current_url + "\">Link</a>"
            except:
                pass
    driver.close()
    return source_links

def categorize_leans(pod_bias_df, partisan_database):
    '''
    Categorize each row of pod_bias_df based on partisan leans stored in partisan_database dict.
    If unable to label, classify as "Neither".
    Will add new column named "Partisan Leans" to store the data.
    Returns modified df.
    '''
    # For show names like 'The Dan Bongino Show'
    isolate_name = re.compile(r"^[Tt]he\s+|\S?[Ss]how\S?|\S?[Pp]odcast\S?|\s[Rr]adio$")
    for index, row in pod_bias_df.iterrows():
        # Clean names -- spotify charts has title formatting
        channel_class = partisan_database.get(row[0].strip())
        name_class = partisan_database.get(re.sub(isolate_name, "", row[1]).strip())
        # labels by podcast name first, if possible, then by channel name
        if name_class != None:
            pod_bias_df.loc[index, "Partisan Lean"] = name_class
        elif channel_class != None:
            pod_bias_df.loc[index, "Partisan Lean"] = channel_class
        else:
            pod_bias_df.loc[index, "Partisan Lean"] = "Neither"
    return pod_bias_df

######################################################
# Main
######################################################

start_date = "Jun 16 2021"
daily_charts = []
for day in pd.date_range(start_date, end_date):
    key_format = day.strftime('%b%d%y')
    # see if chart for given day exists
    try:
        df = pd.read_hdf("spotify_podcasts.h5", key=f"{key_format}")
        day_df = (
            pd.concat([df, pd.DataFrame({"Date": len(df)*[day]})], axis=1)
        )
        daily_charts.append(day_df)
    except KeyError:
        pass
combined_df = pd.concat(daily_charts)

with open('podcast_day_data/partisan_database.pkl', 'rb') as f:
    partisan_database = pickle.load(f)

with open('podcast_day_data/source_list.pkl', 'rb') as f:
    source_list = pickle.load(f)

# To restart:
# partisan_database = dict()
# source_list = dict()

sources = list(combined_df["Source"].values)
source_list.update(find_biases_dict(sources, partisan_database))
pod_bias_df = combined_df.reset_index().rename(columns={"index": "Rank"}).set_index(["Date", "Rank"]) # with no duplicate indices
categorize_leans(pod_bias_df, partisan_database)

with open('podcast_day_data/partisan_database.pkl', 'wb') as f:
    pickle.dump(partisan_database, f)

with open('podcast_day_data/source_list.pkl', 'wb') as f:
    pickle.dump(source_list, f)

##### Save current day "Neither" table
pod_neither_df = (pod_bias_df.reset_index()
                  .drop(columns=["Date", "Rank"])
                  .drop_duplicates()
                  .query("`Partisan Lean` == 'Neither'")
                 )
pod_neither_df.to_html(f"podcast_day_data/today_neither", index=False)

# find classification for all political podcasts
pod_political_df = (pod_bias_df.reset_index()
                    .drop(columns=["Date", "Rank"])
                    .drop_duplicates()
                    .sort_values("Source")
                    .query("`Partisan Lean` != 'Neither'")
                   )
pod_political_df.to_html("podcast_day_data/all_pods_partisan_leans", index=False) # don't print numbers; they're not relevant with given transforms

# counts number of podcasts with given partisan leans per day,
# setting multiindex with outer layer as date and inner as partisan lean
partisan_daily_count = (pod_bias_df.reset_index()[["Date", "Partisan Lean"]]
                        .groupby(["Date", "Partisan Lean"])
                        .size().to_frame("Count")
                       )
# get avg number of leans for each podcast everyday & percent distribution for each political lean
partisan_daily_count.groupby("Partisan Lean").mean().to_html("podcast_day_data/temporal_avg_leans_per_day")
mean_pods = partisan_daily_count.groupby("Partisan Lean").mean().drop("Neither")
(mean_pods/mean_pods.sum()).to_html("podcast_day_data/temporal_mean_leans_percent")

##### Creates current day graph

colors_dict = {"Left": "#0015BC", "Center": "#301934", "Right": "#DE0100", "Neither": "lightgrey"}
line_order = ["Left", "Center", "Right", "Neither"]
colors = [colors_dict.get(l) for l in line_order]

fig, ax = plt.subplots(figsize=(8, 4))
current_day_df = pod_bias_df.loc[pd.to_datetime(end_date), :].groupby("Partisan Lean").size()[line_order]

current_day_df.plot(ax=ax, kind="bar", color=colors, title=f"{end_date.strftime('%b %d, %Y')}\nSpotify Top 50 US News Podcasts by Political Lean",
      xlabel="", zorder=2) # place above grid

remove_spines(ax)
ax.grid(axis="y", alpha=0.2)
ax.tick_params(axis="x", labelrotation=0)
ax.set_facecolor(facecolor)
fig.savefig(f"podcast_day_data/podcast_leans_today.png", dpi=200)

# Show distribution of current day's podcasts belonging to each political lean
(current_day_df.drop("Neither")/current_day_df.drop("Neither").sum()).to_frame("Fraction").to_html(f"podcast_day_data/today_political_distribution")


##### Creates throughout time graphs

fig, ax = plt.subplots()
# Reorder
partisan_count_graph = partisan_daily_count.unstack().reindex(line_order, axis=1, level=1)
partisan_count_graph.plot(ax=ax, color=colors)

# Isolate inner index values (partisan lean) for legend labels and place below figure
handles, labels = ax.get_legend_handles_labels()
real_labels = [l[:-1].split(", ")[1] for l in labels]
# fig.subplots_adjust(top=0.1)
ax.legend(handles, real_labels, ncol=4, loc="center", bbox_to_anchor=(0.5, 1.07), fancybox=True, shadow=True)

# if there are less than 8 days, set xticks to be everyday
time_range = pd.date_range("Jun 16, 2021", end_date)
if len(time_range) <= 8:
    ax.set_xticks(time_range)

ax.xaxis.set_major_formatter(mdates.DateFormatter(r"\text{%b}\;%d,\;%Y"))

remove_spines(ax)
ax.set_ylabel("Number of Podcasts")
ax.set_title(r"\textbf{Spotify Top 50 US News Podcasts by Political Lean}", pad=30)

time_offset = pd.Timedelta(1, "hour")
for lean in ["Left", "Right", "Center", "Neither"]:
    last_pt = partisan_daily_count.unstack().iloc[-1, :].loc[:, [lean]]
    ax.annotate(lean, xy=(last_pt.name, last_pt[0]),
                xytext=(last_pt.name + time_offset, last_pt[0]))
fig.tight_layout()
fig.savefig(f"podcast_day_data/temporal_leans_until_today.png", dpi=200)
