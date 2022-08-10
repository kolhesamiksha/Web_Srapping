# Web_Scrapping

## What Is Webscraping:
Web scraping (or data scraping) is a technique used to collect content and data from the internet. This data is usually saved in a local file so that it can be manipulated and analyzed as needed. If you’ve ever copied and pasted content from a website into an Excel spreadsheet, this is essentially what web scraping is, but on a very small scale.

However, when people refer to ‘web scrapers,’ they’re usually talking about software applications. Web scraping applications (or ‘bots’) are programmed to visit websites, grab the relevant pages and extract useful information. By automating this process, these bots can extract huge amounts of data in a very short time. This has obvious benefits in the digital age, when big data—which is constantly updating and changing—plays such a prominent role.


### Github Topics and trendings scraping using BeautifulSoup

![image](https://user-images.githubusercontent.com/73512374/179812663-83e176fd-6174-4eac-9fa0-b648bbded4d4.png)

In this POC project mostly focused on web navigation and learned how to extract the data from the web/URL's.
1. Parsed Github topics and trendings URL using html parser.
2. the Html page get parsed using beautifulSoup coz, It provides a set of well defined methods for extracting information contained within HTML tags in a website.
3. after inspecting the webpage and going under the tags using findall() gave the informative data.
4. After collecting topics and trendings data this get converted into .csv file so that data become analytics/industry ready.

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

Finally, Winner YouTube Channel is 3Blue1Brown🎉🎉

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
