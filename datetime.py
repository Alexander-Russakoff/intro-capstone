import datetime

date = datetime.date.today()


#2 WEEKS METHOD
def getSundayAfterNext():
  day = date.weekday()
  #add the first guaranteed week of days
  change = 7

  #if sunday, just look at next two weeks easy
  if day == 6:
    change += 6
  #if monday, add 6 days to next Sunday
  #same for other days, but reduce 1
  else:
    for i in range(6):
      if day == i:
        change += 6-i
        break

  #create new date change and set it appropriately
  cutOff = date + datetime.timedelta(days = change)

  return cutOff

endDate = getSundayAfterNext()





#VALID DAY METHOD
def isValidDay(string, cutoff):
  temp = string.split("-")
  #convert to int in most nasty way imaginable
  for i in range(len(temp)):
    temp[i] = int(temp[i])

  tempDay = datetime.date(temp[0], temp[1], temp[2])
  
  return date <= tempDay and cutoff > tempDay

print(isValidDay("2023-01-12",endDate))
print(isValidDay("2023-01-24",endDate))
print(isValidDay("2023-01-30",endDate))



def removeEventNotWithinTwoWeeks(dictList):
  eventsWithinTwoWeeks = []  
  for i in range(len(dictList)):
    if isValidDay(dictList[i]["event_date"] , endDate):
      print(dictList[i]["event_date"])
      eventsWithinTwoWeeks.append(dictList[i])
      
  print(*eventsWithinTwoWeeks, sep="\n\n")

  return eventsWithinTwoWeeks

