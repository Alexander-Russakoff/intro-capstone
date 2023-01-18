#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 09:46:10 2023

@author: alex
"""


import datetime




#2 WEEKS METHOD
def getSundayAfterNext():
  day = datetime.date.today().weekday()
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
  cutOff = datetime.date.today() + datetime.timedelta(days = change)

  return cutOff


#VALID DAY METHOD
def isValidDay(string, cutoff):
  
  date = datetime.date.today()
  temp = string.split("-")
  #convert to int in most nasty way imaginable
  for i in range(len(temp)):
    temp[i] = int(temp[i])

  tempDay = datetime.date(temp[0], temp[1], temp[2])
  
  return date <= tempDay and cutoff > tempDay

def removeEventNotWithinTwoWeeks(dictList):
  endDate = getSundayAfterNext()
  eventsWithinTwoWeeks = []  
  for i in range(len(dictList)):
    if isValidDay(dictList[i]["event_date"] , endDate):
      print(dictList[i]["event_date"])
      eventsWithinTwoWeeks.append(dictList[i])

  print(*eventsWithinTwoWeeks, sep="\n\n")

  return eventsWithinTwoWeeks

