Name: Nadeem Sousaf

Program Description: This program scrapes the Government of Canada's weather forecast webpage for Ottawa, ON. The data is displayed upon executing the program.

Execution Instructions: Enter the command "python main.py" into a terminal that has been opened in the directory containing the file "main.py".

Message to Reader: This program is heavily hardcoded, as in, there are many variables used that are specific to the webpage itself. Should those variables change by name or format, the code will fail and need to be updated to compensate for these changes.

Message to Self: Look into XML files, try to improve efficiency when scraping to pull less data as entire HTML not needed.

File Overview:
main.py - control flow of program with error handlin
helper.py - helper functions used in main.py
table_manager.py - contains code for sqlite3 table used in main.py