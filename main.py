
from helper import *


def init():
    try:
        table_var = make_table()
        mycursor = table_var[0]
        myconnect = table_var[1]
        webpage_data = search()
        if webpage_data != ERR_NOT_FOUND: #check this
            json_data = webpage_data[0]
            current_temp = webpage_data[1]
            headers = json_data.keys()
            data = script_walk(json_data)
            add_all_data(data,mycursor)
            print_forecast(mycursor)
            
    except:
        print("Error parsing webpage metadata, exiting program")
        return ERR_NOT_FOUND
        exit()
        
    myconnect.close()


init()




