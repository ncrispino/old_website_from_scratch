import pickle
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

# Extract top 50 news podcasts, according to the spotify charts
url_pod = "https://chartable.com/charts/spotify/united-states-of-america-news-politics"
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("C:/Users/ncris/econ/chromedriver_win32/chromedriver.exe", options=options)
driver.get(url_pod)
soup_pod = BeautifulSoup(driver.page_source, "lxml")
driver.close()

pod_details = [] # appended in order
pod_table = soup_pod.body.find("table")
for row in pod_table.find_all("tr"):
#     number = row.find("div", {"class" : "b header-font f2 tc"}).text
    description = row.find("td", {"class" : "pv2 ph1"}).text
    pod_details.append(description[1:-1].split("\n"))
pod_details
pod_df = pd.DataFrame(pod_details, columns=["Source", "Name"])
# Replace None values in podcast name with the source of the podcast
pod_df.loc[pod_df["Name"].isnull(), "Name"] = pod_df.loc[pod_df["Name"].isnull(), "Source"]

# Create date shortname for key of table in hdf file
today_date_short = date.today().strftime('%b%d%y')
# append current day's dataframe to file
pod_df.to_hdf("spotify_podcasts.h5", key=f"{today_date_short}", mode="a")
