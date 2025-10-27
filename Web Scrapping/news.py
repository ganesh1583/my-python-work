from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime

date = datetime.now().date().strftime("%Y-%m-%d")
fname = date+".txt"
f = open(fname,"w",encoding="utf-8")
f.write(date+"\n\n\n")


url = "https://www.hindustantimes.com"
url_responce = urlopen(url)
page_data = url_responce.read()
url_responce.close()

page_html_data = BeautifulSoup(page_data,"html.parser")

data = page_html_data.find_all("div",{"class":"htImpressionTracking"})
j = 1
for i in data:
	label = "News nunber : "+str(j)+"\n\n"
	f.write(label)
	f.write(i.text+"\n\n")
	j+=1


f.write("The End \n")
f.close()
print("File Created Successfully !!!")