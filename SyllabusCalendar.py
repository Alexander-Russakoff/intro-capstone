# -*- coding: utf-8 -*-
"""
Standalone Syllabus Calendar        
"""


import requests 


import tkinter as tk
#from tkinter import ttk
from tkinter import scrolledtext
from DateBounder import removeEventNotWithinTwoWeeks




def makeRequest():

    headers = {"Authorization": "Bearer PU4UGN2sUPaEG1yw1CmOuyzX2DhhDeC2G6OLHn97",
        "Content-Type" : "application/json",
        "Accept": "application/json"}
    
    url = "https://courses.ianapplebaum.com/api/syllabus/1"
    
    r = requests.get(url,headers=headers)
    
    #print(r.status_code)
    #print(r.text)
    #print(r.json())
    if r.status_code == 200:
        request = r.json()
        return request['events']
    
    return None

#update the text based on event type
def updateText(calendar,events,eventType):
    calendar.configure(state='normal')
    calendar.delete(1.0,tk.END)
    calendar.insert(tk.END,eventsByType(events,eventType))
    print(eventsByType(events,eventType))
    calendar.configure(state='disabled')
    calendar.tag_add("text_highlight", "1.0", "end")
#return an event of a specific type
#allowed types: assignment lecture lab sprint break
def eventsByType(events,eventType):
    return prettyPrint([x for x in events if x['class_type']==eventType])
    

def prettyPrint(events):
    DATE_KEY = 'event_date'
    NAME_KEY = 'event_name'
    DESCRIPTION_KEY = 'event_description'
    TYPE_KEY = 'class_type'
    
    temp = ""
    for x in events:
        temp = temp + x[DATE_KEY] + " | " + x[NAME_KEY] +" | "+ x[TYPE_KEY]+ "\n\n" + x[DESCRIPTION_KEY]+"\n\n"
    return temp

print("Begin")

#get all events
events_all = makeRequest()
#get all events for this week and the following week
events = removeEventNotWithinTwoWeeks(events_all)

text = prettyPrint(events)

print(text)



root = tk.Tk()

root.title("Capstone Calender")
root.geometry("800x500")
#labButton = ttk.Button
calendar = scrolledtext.ScrolledText(root,font={"Arial Bold",20},width=78,height=24)#,wrap=tk.WORD)
#calendar.winfo_geometry("800x450")
buttonFrame = tk.Frame(root)


assignmentButton = tk.Button(buttonFrame, text="Assignments", font = ("Helvetica", 15, "bold"), command =lambda: updateText(calendar,events_all,"Assignment"))
lectureButton = tk.Button(buttonFrame, text="Lectures", font = ("Helvetica", 15, "bold"), command =lambda: updateText(calendar,events_all,"Lecture"))
labButton = tk.Button(buttonFrame, text="Labs", font = ("Helvetica", 15, "bold"),  command =lambda: updateText(calendar,events_all,"Lab"))
sprintButton = tk.Button(buttonFrame, text="Sprints", font = ("Helvetica", 15, "bold"), command=lambda: updateText(calendar,events_all,"Sprint"))
breakButton = tk.Button(buttonFrame, text="BREAK", font = ("Helvetica", 15, "bold"), command=lambda: updateText(calendar,events_all,"Break"))

calendar.tag_config("text_highlight", font=("Arial Bold",12))

calendar.insert(tk.INSERT,text)
calendar.configure(state="disabled")

calendar.tag_add("text_highlight", "1.0", "end")

calendar.grid(row=0,column=0)

assignmentButton.grid(row=0,column=0,sticky='W')
lectureButton.grid(row=0,column=1,sticky='W')
labButton.grid(row=0,column=2,sticky='W')
sprintButton.grid(row=0,column=3,sticky='W')
breakButton.grid(row=0,column=4,sticky='W')

buttonFrame.grid(row=1,column=0,sticky='W')
#calendar.delete(1.0,tk.END)
#calendar.insert(tk.END, eventsByType(events_all,"Assignment"))
root.mainloop()

prettyPrint(events)
