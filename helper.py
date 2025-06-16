def format_check(list,i):
    if 'date' in list[i] and 'summary' in list[i] and 'temperatureText' in list[i] and 'titleText' in list[i]:
        return True
    else:
        return False
    
def print_forecast(list):
    print('placeholder')