def add_time(start, duration, day = ''): #add_time("11:59 PM", "24:05", "Wednesday")
    days = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thusday',
        'Friday',
        'Saturday',
    ]

    startAbrev = start.split(' ')[1]
    startTime = start.split(' ')[0].split(':')
    durationTime = duration.split(':')
        
    minutes = int(startTime[1]) + int(durationTime[1])
    hours = int(startTime[0]) + int(durationTime[0])
    nextDay = 0;
    nextDayText = ""
    if(minutes > 60):
        minutes -= 60
        hours += 1

    
    if(hours >= 12):
        while(hours >= 12):
            hours = hours - 12

            if(startAbrev == 'AM'):
                startAbrev = 'PM'
            else:
                startAbrev = 'AM'
                nextDay += 1
            
        if(hours == 0):
            hours = 12

    if(day != ''):
        index = 0
        for i in days:
            if(i.lower() != day.lower()):
                index += 1
            else:
                break
    

        indexDay = nextDay
        while(indexDay > 0):
            indexDay -= 7
        
        if(index + indexDay > 6):
            index = index + indexDay -7
            nextDayText = ", " + days[index]
        else:
            nextDayText = ", " + days[index + indexDay]
        # print(nextDayText)
        # print(index + indexDay)
        # # print(days[index + indexDay])
        # print(nextDay)
        # print(indexDay)
    
    if(nextDay == 1):
        nextDayText += " (next day)"
    elif(nextDay > 1):
        nextDayText += " (" + str(nextDay) + " days later)"
    else:
        nextDayText += ""

    
    if(minutes < 10):
        minutes = str(0) + str(minutes)
    
    print(str(hours) + ":" + str(minutes) + " " + startAbrev + nextDayText)
    
    return str(hours) + ":" + str(minutes) + " " + startAbrev + nextDayText