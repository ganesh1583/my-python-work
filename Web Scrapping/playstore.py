from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

url = "https://play.google.com/store/games"
url_req = urlopen(url)
page = url_req.read()
url_req.close()

html_data = BeautifulSoup(page,"html.parser")
print(html_data)
