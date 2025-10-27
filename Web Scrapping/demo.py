from bs4 import BeautifulSoup
from urllib.request import urlopen


f = open("top_movies.csv","w")
header = "Movie Name\n"
f.write(header)

url = "https://www.timeout.com/film/best-movies-of-all-time"
url_responce = urlopen(url)
page_info = url_responce.read()
url_responce.close()


page_html_info = BeautifulSoup(page_info,"html.parser")

boxes = page_html_info.find_all("div",{"class":"articleContent _articleContent_kc5qn_216"})

#print(len(boxes))

#print(boxes[0].div.a.h3.text)
for box in boxes:
    f.write(box.div.a.h3.text+"\n")
f.close()
