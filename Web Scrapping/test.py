from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


search_str = input("Which product you want to search : ")
filename = search_str+".csv"

flipkart_url = "https://www.flipkart.com/search?q=" + search_str

url_req = urlopen(flipkart_url)
flipkart_page = url_req.read()
url_req.close()

flipkart_html = BeautifulSoup(flipkart_page,"html.parser")

boxes = flipkart_html.find_all("div",{"class" : "_1AtVbE col-12-12"})

for b in boxes:
	print(b)