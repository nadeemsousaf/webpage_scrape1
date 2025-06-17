import sqlite3

'''
connect_db = sqlite3.connect("forecast.db")
cursor = connect_db.cursor()
cursor.execute("DROP TABLE IF EXISTS FORECAST")
table = """ CREATE TABLE FORECAST (
            Date VARCHAR(255) NOT NULL,
            High INT,
            Low INT,
            DaySummary VARCHAR(255),
            NightSummary VARCHAR(255)
        ); """
cursor.execute(table)
#connect_db.close() #put in main.py

def add_table_data(list,i):
    #date_list.append({'date':location[i]['date'],'summary':location[i]['summary'],'high':location[i]['temperatureText']})
    
    if "High" is in location[i]['temperatureText']:
        #high value
    else:
        #low value

    #if location[i]['periodLabel'] == "Night"

'''