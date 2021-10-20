import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import re

#to get the URL
url = "https://github.com/topics"
response = requests.get(url)

#Check the url is working or not
if(response.status_code!=200):
    print("Error!")

#To get the Content of Website
texts = response.text
bsoup = bs(texts,"html.parser")

#To get the content of Topics Block
div_class = bsoup.find_all("div",{"class":"py-4 border-bottom"})

#For lists creation
Title = []
Description = []

for i in range(len(div_class)):
    
    #To get the names of trending topics in a-tag
    title = div_class[i].find_all("a",{"class":"d-flex no-underline"})[0].text
    title = re.sub(r'[#]',"",title)
    title = title.strip().replace("   "," ")
    title = title.split("\n\n")
    Title.append(title[0])


    #To get the description of the topics
    des = title[1:2]
    des = [x.strip() for x in des]
    Description.extend(des)

#Dict for further dataframe conversion
Topics_dict = {
    "Title of Topics":Title,
    "Description":Description
}

#Dataframe 
tp_frame = pd.DataFrame(Topics_dict)

#Topics_Csv file
Topics_csv = tp_frame.to_csv("Trending Topics Scrapping.csv")
