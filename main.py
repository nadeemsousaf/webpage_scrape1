import requests
from bs4 import BeautifulSoup
import json
import re

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

#print(json_data)
headers = json_data.keys()
#print(list(headers))
#['relOrigin', 'breadcrumbs', 'topBanners', 'bottomBanners', 'pageDtIso', 'alert', 'city', 'map', 'location', 'myweatherprofile', 'technicalDiscussion', 'route']
location = json_data['location']
#print(location)
location = (location['location'])
location = (location['45.40300000--75.68700000'])
location = location['forecast']
location = location['daily']
#print(type(location))
#print(location)

#'date', 'summary', 'periodLabel', periodID', 'temperatureText', 'titleText'
#{location[i]['date'],location[i]['summary'],location[i]['periodLabel'],location[i]['periodID'],location[i]['temperatureText'],location[i+1]['titleText']}
date_list = []
i = 0

while i < len(location):
    if type(location[i]) is dict:
        if 'date' in location[i] and 'summary' in location[i] and 'periodLabel' in location[i] and 'temperatureText' in location[i] and 'titleText' in location[i]:
            comma_loc = location[i]['periodLabel'].find(",")
            if comma_loc != -1:
                location[i]['periodLabel'] = location[i]['periodLabel'][0:comma_loc]
            date_list.append({'date':location[i]['date'],'summary':location[i]['summary'],'weekday':location[i]['periodLabel'],'high':location[i]['temperatureText'],'titleText':location[i]['titleText']})
    i+=2

#print(date_list)
for i in range (len(date_list)):
    print("Date: ", date_list[i]['date'], "(", date_list[i]['weekday'], ")", "\n")
    print("Summary: ", date_list[i]['summary'], "\n")
    #print(date_list[0].keys())
#['date', 'summary', 'periodID', 'periodLabel', 'windChill', 'sun', 'temperatureText', 'humidex', 'precip', 'frost', 'titleText', 'temperature', 'iconCode', 'text']

print(date_list)



