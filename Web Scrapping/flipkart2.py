from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

#search_str = input("Enter which product you want to search : ")
search_str = "oneplusnord2t"
filename = search_str + ".csv"

fw = open(filename,"w",encoding="utf-8")
header = "Product, Customer Name, Rating, Heading, Comment \n"
fw.write(header)

flipkart_url = "https://www.flipkart.com/search?q=" + search_str


url_req = urlopen(flipkart_url)
flipkart_page = url_req.read()
url_req.close()

flipkart_html = BeautifulSoup(flipkart_page,"html.parser")

boxes = flipkart_html.find_all("div",{"class":"_1AtVbE col-12-12"})

del boxes[0:3]
box = boxes[0]

prod_link = "https://www.flipkart.com" + box.div.div.div.a["href"]
prod_res = requests.get(prod_link)
prod_res.encoding = "utf-8"

prod_html = BeautifulSoup(prod_res.text,"html.parser")



commentboxes = prod_html.find("div",{"class":"_2MImiq _1Qnn1K"})

#del commentboxes[-1]
print(commentboxes.span.nav['class'])

