import sqlite3

None_placeholder = "None"

connect_db = sqlite3.connect("forecast.db")
mycursor = connect_db.cursor()
mycursor.execute("DROP TABLE IF EXISTS FORECAST")
table = """ CREATE TABLE FORECAST (
            Date VARCHAR(255) NOT NULL,
            High INT,
            Low INT,
            DaySummary VARCHAR(255),
            NightSummary VARCHAR(255)
        ); """
mycursor.execute(table)
#connect_db.close() #put in main.py

def check_exists(date):
    mycursor.execute("SELECT * from FORECAST where Date = ?", (date,))
    result = mycursor.fetchall()
    if (len(result) < 1):
        return False
    else:
        return result

def add_table_row(insert_tuple):
    query_result = check_exists(insert_tuple[0])
    #print(query_result)
    if query_result != False:
        insert_list = []
        i = 0
        while i < len(query_result[0]):
            if (insert_tuple[i] == None_placeholder):
                insert_list.append(query_result[0][i])
            else:
                insert_list.append(insert_tuple[i])
            i+=1
        #print(insert_list)
        mycursor.execute("UPDATE FORECAST SET High=?, Low=?, DaySummary=?, NightSummary=? WHERE Date=?", (insert_list[1],insert_list[2],insert_list[3],insert_list[4],insert_list[0],))
    else:
        mycursor.execute("INSERT INTO FORECAST (Date, High, Low, DaySummary, NightSummary) VALUES (?,?,?,?,?)", (insert_tuple[0],insert_tuple[1],insert_tuple[2],insert_tuple[3],insert_tuple[4],))

def get_all_data():
    mycursor.execute("SELECT * FROM FORECAST")
    return mycursor.fetchall()



