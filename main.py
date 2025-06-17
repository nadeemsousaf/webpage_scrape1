import requests
from bs4 import BeautifulSoup
import json
import re
from helper import *
from table_manager import *

ERR_OK = 200
ERR_NOT_FOUND = 404


URL = "https://weather.gc.ca/en/location/index.html?coords=45.403,-75.687"
req = requests.get(URL)
#print(req.content)
soup = BeautifulSoup(req.content, 'html5lib')
text = 'window.__INITIAL_STATE__'
fore_script = soup.find_all(lambda tag: tag.name == "script" and text in tag.text)

script_tags = []
for s in soup.find_all('script'):
    script_tags.append(str(s))

json_data = ""

current_temp = ""
soup1 = BeautifulSoup(str(soup.find_all(lambda tag: tag.name == "details" and "Current Conditions" in tag.text)), 'html.parser')
for dt in soup1.find_all(lambda tag: tag.name == "dt" and "Temperature" in tag.text):
    dd = dt.find_next_sibling('dd')
    if dd:
        current_temp = dd.get_text(strip=True)


for s in script_tags:
    try:
        if 'window.__INITIAL_STATE__' in s:
            match = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.*\});', s, re.DOTALL)
            json_string = match.group(1)
            json_data = json.loads(json_string)
            
    except:
        pass

try:
    if json_data != "":
        print("ok")

except:
    print("Error parsing webpage metadata, exiting program")
    exit()

headers = json_data.keys()
#print(list(headers))
#['relOrigin', 'breadcrumbs', 'topBanners', 'bottomBanners', 'pageDtIso', 'alert', 'city', 'map', 'location', 'myweatherprofile', 'technicalDiscussion', 'route']
location = json_data['location']
#print(location)
location = (location['location'])
location = (location['45.40300000--75.68700000'])
location = location['forecast']
#print(location.keys())
#print(location['dailyIssuedTimeShrt'])
location = location['daily']

#'date', 'summary', periodID', 'temperatureText', 'titleText'
#{location[i]['date'],location[i]['summary'],location[i]['periodLabel'],location[i]['periodID'],location[i]['temperatureText'],location[i+1]['titleText']}
date_list = []

i = 0
while i < len(location):
    if type(location[i]) is dict:
        if format_check(location,i):
            date_list.append({'date':location[i]['date'],'summary':location[i]['summary'],'high':location[i]['temperatureText'], 'periodLabel':location[i]['periodLabel']})
    i += 1


for i in range (len(date_list)):
    print("Date: " + date_list[i]['date'] + "\n")
    print("Summary: " + date_list[i]['summary'] + "\n")
    print("High/Low: " + date_list[i]['high'] + "0°C\n")


#['date', 'summary', 'periodID', 'periodLabel', 'windChill', 'sun', 'temperatureText', 'humidex', 'precip', 'frost', 'titleText', 'temperature', 'iconCode', 'text']

#print(date_list)

print(current_temp)




