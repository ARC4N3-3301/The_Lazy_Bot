import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def page(arg1, arg2):
    url = arg1
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    var = arg2
    text_list = []
    try:
        for paragraph in range(0, var):
        	info = soup.find_all('p')[paragraph].get_text()
        	text_list.append(info)
        return text_list
    except IndexError:
    	return False

