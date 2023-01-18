# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import json
import requests 
import datetime
import pprint

import tkinter as tk
from tkinter import scrolledtext
  

def makeRequest():

    headers = {"Authorization": "Bearer PU4UGN2sUPaEG1yw1CmOuyzX2DhhDeC2G6OLHn97",
        "Content-Type" : "application/json",
        "Accept": "application/json"}
    
    url = "https://courses.ianapplebaum.com/api/syllabus/1"
    
    r = requests.get(url,headers=headers)
    

    if r.status_code == 200:
        request = r.json()
        return request['events']
    
    return None

def dateRange():
    pass

def prettyPrint(events):
    DATE_KEY = 'event_date'
    NAME_KEY = 'event_name'
    DESCRIPTION_KEY = 'event_description'
    
    temp = ""
    for x in events:
        temp = temp + x[DATE_KEY] + " | " + x[NAME_KEY] + "\n\n" + x[DESCRIPTION_KEY]+"\n\n"
    return temp

print("Begin")

events = makeRequest()

text = prettyPrint(events)

print(text)

root = tk.Tk()

root.title("Capstone Calender")
root.geometry("600x400")
calendar = scrolledtext.ScrolledText(root,font={"Arial Bold",20})#,wrap=tk.WORD)
calendar.insert(tk.INSERT,text)
#calendar.configure(state="disabled")
calendar.pack()

root.mainloop()

prettyPrint(events)
