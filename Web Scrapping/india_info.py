from bs4 import BeautifulSoup
from urllib.request import urlopen

#f = open("india.txt","w",encoding="utf-8")

url = "https://en.wikipedia.org/wiki/India"
url_resp = urlopen(url)
page_data = url_resp.read()
url_resp.close()

html_data = BeautifulSoup(page_data,"html.parser")

data = html_data.find_all("div",{"class":"mw-parser-output"})

print(data)

#f.close()