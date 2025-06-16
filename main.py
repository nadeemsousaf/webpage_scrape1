import sqlite3
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/canadian-intellectual-property-statistics/ip-horizons-download-intellectual-property-data"
req = requests.get(URL)
print(req.content)
rep_ptree = BeautifulSoup(req.content, 'html5lib')
