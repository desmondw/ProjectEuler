daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#refDate = [1, 1, 1900] #day, month, year
#refDay = 2 #Sunday = 1, Saturday = 7

startDate = [1, 1, 1901] #day, month, year
endDate = [31, 12, 2000] #day, month, year
startDay = 3 #Sunday = 1, Saturday = 7
dayOfWeek = startDay
sundaysOnFirst = 0

def processDays(startDate, endDate):
    global dayOfWeek, sundaysOnFirst, daysInMonth
    for year in range(startDate[2], endDate[2] + 1): #for each year
        if year == startDate[2]:
            monthStart = startDate[1]
        else:
            monthStart = 1
        if year == endDate[2]:
            monthEnd = endDate[1]
        else:
            monthEnd = 12

        for month in range(monthStart, monthEnd + 1): #for each month
            if year == startDate[2] and month == startDate[1]:
                dayStart = startDate[0]
            else:
                dayStart = 1
            if year == endDate[2] and month == endDate[1]:
                dayEnd = endDate[0]
            else:
                dayEnd = daysInMonth[month-1]

            for day in range(startDate[0], dayEnd + 1): #for each day
                #if sunday and first of the month, add to counter
                if dayOfWeek == 1 and day == 1:
                    sundaysOnFirst += 1

                #progress day of week
                if dayOfWeek == 7:
                    dayOfWeek = 1
                else:
                    dayOfWeek += 1

processDays(startDate, endDate)
print "Sundays on the first: " + str(sundaysOnFirst)