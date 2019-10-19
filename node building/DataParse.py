# author timothy vitkin
import requests
import urllib.request
import time
import json
from bs4 import BeautifulSoup
url = 'http://catalog.illinois.edu/courses-of-instruction/cs/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
courses = soup.findAll("div", class_="courseblock")
for course in courses:
    data = {}