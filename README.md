# Web_Srapping



### Github Topics and trendings scraping using BeautifulSoup

![image](https://user-images.githubusercontent.com/73512374/179812663-83e176fd-6174-4eac-9fa0-b648bbded4d4.png)


1. Parsed Github topics and trendings URL using html parser coz, webpage used to be in html.
2. parsed data get converted into beautifulSoup format it provides ways of navigating, searching, and modifying the parse tree.
3. after inspecting the webpage and going under the tags using findall() gives the us the data.
4. extracted data get converted into dataFrame hence .csv file.

### Best Data Science Channel on Youtube webscraping using Youtube API

![image](https://user-images.githubusercontent.com/73512374/179812470-387b579b-d9cb-43c3-ab25-f2379c4859fa.png)


In this Task using youtube api and best data science youtubers channel id's are collected & about 10 best recommended channels are selected. After that googleapiclient method has a module built that scrapes the channel data into json format/Dictionary and then converted into DataFrame.did Data Visualization over the collecetd data.
The best of best youtube channel is chosen as per the viewers, subscribers, likes, dislikes, no_of_videos uploaded, year of start etc...

1. created A Youtube API acess key/developer key for Youtube using google cloud
2. how to create that access api is as follows.
* Create a project on API and services.
![image](https://user-images.githubusercontent.com/73512374/179802244-c7d34076-92fd-4c2c-8171-93418629f153.png)
* next go to credentials and click on create Credentials. search for Youtube API V3 over the search box and click enable. the developer key will be generated
![image](https://user-images.githubusercontent.com/73512374/179803617-12de0760-9c44-4ccd-ad29-6bf9b8bb9dea.png)
* Using that key youtube channel get parsed -> Scraped -> DataFrame.
* Likewise Each Youtube Channel data get scraped over videos, playlists and channels.
* Did data analysis by considering year of start, likes, viewers to each video, dislikes etc.
All methods are in detailed explained in the .ipynb file:)

Finally, Winner YouTube Channel is 3Blue1Brown????????

Reference: Youtube API working developers Platform https://developers.google.com/youtube/v3/docs 


Tools Used:
1. Google Cloud
2. Google Colab.
3. Json Formatter.

Libraries Used
1. BeautifulSoup
2. googleapiclient
3. Pandas
4. Numpy
