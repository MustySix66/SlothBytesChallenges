def convertTime(time):
    leng = time.split()
    # check if (am, pm) exists
    if len(leng) == 2:
        hour, period = leng
        hour, minutes = map(int, hour.split(":"))
        
        if period == "am":
            if hour == 12:
                hour = 0
        elif period == "pm":
            if hour != 12:
                hour += 12
        return f"{hour}:{minutes:02}"
    elif len(leng) == 1:  # 24hrs
        hour, minutes = map(int, time.split(":"))
        period = "am" if hour < 12 else "pm"
        if hour == 0:
            hour = 12
        elif hour > 12:
            hour -= 12
        return f"{hour}:{minutes:02} {period}"
    else:
        return "Incorrect hour format."

print(convertTime("12:00 am"))  # "0:00"
print(convertTime("6:20 pm"))   # "18:20"
print(convertTime("21:00"))     # "9:00 pm"
print(convertTime("5:05"))      # "5:05 am"
