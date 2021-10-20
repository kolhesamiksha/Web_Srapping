import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import re

url = "https://github.com/topics"
response = requests.get(url)

if(response.status_code!=200):
    print("Error!")

texts = response.text
bsoup = bs(texts,"html.parser")

div_class = bsoup.find_all("div",{"class":"py-4 border-bottom"})

Title = []
Description = []
for i in range(len(div_class)):
    #title for names of trending topics
    title = div_class[i].find_all("a",{"class":"d-flex no-underline"})[0].text
    title = re.sub(r'[#]',"",title)
    title = title.strip().replace("   "," ")
    title = title.split("\n\n")
    Title.append(title[0])


    #des for title's description
    des = title[1:2]
    des = [x.strip() for x in des]
    Description.extend(des)

Topics_dict = {
    "Title of Topics":Title,
    "Description":Description
}

tp_frame = pd.DataFrame(Topics_dict)

Topics_csv = tp_frame.to_csv("Trending Topics Scrapping.csv")


