from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


search_str = input("Which product you want to search : ")
filename = search_str+".csv"

fw = open(filename,"w",encoding="utf-8")
header = "Product, Customer Name, Rating, Heading, Comment \n"
fw.write(header)


flipkart_url = "https://www.flipkart.com/search?q=" + search_str

url_req = urlopen(flipkart_url)
flipkart_page = url_req.read()
url_req.close()

flipkart_html = BeautifulSoup(flipkart_page,"html.parser")

boxes = flipkart_html.find_all("div",{"class" : "_1AtVbE col-12-12"})


del boxes[0:3]
box = boxes[0]

productLink = "https://www.flipkart.com" + box.div.div.div.a['href']

prod_res = requests.get(productLink)
prod_res.encoding = "utf-8"

prod_html = BeautifulSoup(prod_res.text,"html.parser")



commentboxes = prod_html.find_all("div",{"class":"_16PBlm"})

del commentboxes[-1]

for commentbox in commentboxes:
	try:
		name = commentbox.div.div.find_all("p",{"class": "_2-N8zT"})
		commenthead = name[0].text

		rating = commentbox.div.div.div.div.text
		
		name = commentbox.div.div.find_all("p",{"class" : "_2sc7ZR _2V5EHH"})[0].text

		comtag = commentbox.div.div.find_all("div",{"class": ""})
		custcomment = comtag[0].div.text		


		fw.write(search_str+", "+name+", "+rating+", "+commenthead+", "+custcomment+" \n")

	except Exception as e:
		print(e)


fw.close()
print(search_str+".csv is  created !!!")