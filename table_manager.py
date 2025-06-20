import sqlite3


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

def check_exists(date):
    cursor.execute("SELECT Date from table WHERE Date = %s", date)
    result = cursor.fetchall()
    if (len(result) < 1):
        return False
    else:
        return result

def add_table_row(insert_tuple):
    query_result = check_exists(insert_tuple[0])
    if query_result != False:
        insert_list = [insert_tuple[0]]
        i = 0
        while i < len(query_result):
            if (insert_tuple[i] == None):
                insert_list.append(query_result[i])
            else:
                insert_list.append(insert_tuple[i])
        cursor.execute("UPDATE table SET High=%d, SET Low=%d, DaySummary=%s, NightSummary=%s WHERE Date=%s", (insert_list[1],insert_list[2],insert_list[3],insert_list[4],insert_list[0]))
    else:
        cursor.execute("INSERT INTO table (Date, High, Low, DaySummary, NightSummary) VALUES (%s,%d,%d,%s,%s)", (insert_tuple[0],insert_tuple[1],insert_tuple[2],insert_tuple[3],insert_tuple[4]))


