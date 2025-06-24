
from helper import *


def init():
    try:
        table_var = make_table()
        mycursor = table_var[0]
        myconnect = table_var[1]
        webpage_data = search()
        if webpage_data != ERR_NOT_FOUND:
            json_data = webpage_data[0]
            current_temp = webpage_data[1]
            data = script_walk(json_data)
            if data != ERR_NOT_FOUND:
                if add_all_data(data,mycursor) != ERR_NOT_FOUND:
                    print_forecast(mycursor,current_temp)
                    myconnect.close()
                    return ERR_OK
                else:
                    print("Error, formatting in structure has changed, exiting program")
            else:
                print("Error walking pulled script data, exiting program")
            
        else:
            print("Error parsing webpage metadata, exiting program")
            
    except:
        print("Error parsing webpage metadata, exiting program")

    myconnect.close()
    return ERR_NOT_FOUND


init()




