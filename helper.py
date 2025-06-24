import re
from table_manager import *
import json
import requests
from bs4 import BeautifulSoup


URL = "https://weather.gc.ca/en/location/index.html?coords=45.403,-75.687"


def search():
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, 'html5lib')
    text = 'window.__INITIAL_STATE__'
    fore_script = soup.find_all(lambda tag: tag.name == "script" and text in tag.text)

    current_temp = "N/A"
    soup1 = BeautifulSoup(str(soup.find_all(lambda tag: tag.name == "details" and "Current Conditions" in tag.text)), 'html.parser')
    for dt in soup1.find_all(lambda tag: tag.name == "dt" and "Temperature" in tag.text):
        dd = dt.find_next_sibling('dd')
        if dd:
            current_temp = dd.get_text(strip=True)

    script_tags = []
    for s in soup.find_all('script'):
        script_tags.append(str(s))

    json_data = "N/A"

    for s in script_tags:
        try:
            if 'window.__INITIAL_STATE__' in s:
                match = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.*\});', s, re.DOTALL)
                json_string = match.group(1)
                json_data = json.loads(json_string)
                return (json_data,current_temp)
                
        except:
            return ERR_NOT_FOUND
        
def script_walk(data):
    data = data['location']
    data = (data['location'])
    data = (data['45.40300000--75.68700000'])
    data = data['forecast']
    data = data['daily']
    return data

def format_check(dict_row):
    if 'date' in dict_row and 'summary' in dict_row and 'temperatureText' in dict_row:
        return True
    else:
        return False #error handle, change this

def prepare_data(dict_row,mycursor):
    if type(dict_row) is dict:
        if format_check(dict_row):
            insert_val = {'Date':dict_row['date'],'DaySummary':None_placeholder,'NightSummary':None_placeholder,'High':None_placeholder,'Low':None_placeholder}
            if ("Night" in dict_row['periodLabel'] or "Tonight" in dict_row['periodLabel']):
                insert_val['NightSummary'] = dict_row['summary']
            else:
                insert_val['DaySummary'] = dict_row['summary']
            if ("High" in dict_row['temperatureText']):
                insert_val['High'] = int(re.search(r'\d+', dict_row['temperatureText']).group())
            else:
                insert_val['Low'] = int(re.search(r'\d+', dict_row['temperatureText']).group())
            insert_tuple = (insert_val['Date'], insert_val['High'], insert_val['Low'], insert_val['DaySummary'], insert_val['NightSummary'])
            add_table_row(insert_tuple,mycursor)
    else:
        pass #contains bools

def add_all_data(list,mycursor):
    i = 0
    while i < len(list):
        prepare_data(list[i],mycursor)
        i += 1


def print_forecast(mycursor):
    data = get_all_data(mycursor)
    for i in range(len(data)):
        print("Date: "+data[i][0]+" | High: "+ str(data[i][1])+"°C | Low: "+str(data[i][2])+"°C | Day Summary: "+data[i][3]+" | Night Summary: "+data[i][4]+"\n")