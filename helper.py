import re
from table_manager import *

def format_check(dict_row):
    if 'date' in dict_row and 'summary' in dict_row and 'temperatureText' in dict_row:
        return True
    else:
        return False #error handle, change this

def prepare_data(dict_row):
    if type(dict_row) is dict:
        if format_check(dict_row):
            insert_val = {'Date':dict_row['date'],'DaySummary':None,'NightSummary':None,'High':None,'Low':None}
            if ("Night" in dict_row['periodLabel'] or "Tonight" in dict_row['periodLabel']):
                insert_val['NightSummary'] = dict_row['summary']
            else:
                insert_val['DaySummary'] = dict_row['summary']
            if ("High" in dict_row['temperatureText']):
                insert_val['High'] = int(re.search(r'\d+', dict_row['temperatureText']).group())
            else:
                insert_val['Low'] = int(re.search(r'\d+', dict_row['temperatureText']).group())
            insert_tuple = (insert_val['Date'], insert_val['High'], insert_val['Low'], insert_val['DaySummary'], insert_val['NightSummary'])
            add_table_row(insert_tuple)
    else:
        pass #contains bools

def add_all_data(list):
    i = 0
    while i < len(list):
        prepare_data(list[i])
        i += 1


def print_forecast(list): #change to pull from database- obsolete
    for i in range (len(list)):
        print("Date: " + list[i]['date'] + "\n")
        print("Summary: " + list[i]['summary'] + "\n")
        print("High/Low: " + list[i]['high'] + "°C\n")