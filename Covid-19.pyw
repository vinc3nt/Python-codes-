import requests
import json
from tkinter import *

window = Tk()

window.title("Covid-19")

window.geometry('220x60')

lbl = Label(window, text="Total active cases:-......")

lbl.grid(column=1, row=0)
lbl2= Label(window, text="")
lbl2.grid(column=1, row=2)

#txt = Entry(window,width=10)

#txt.grid(column=1, row=0)

def clicked():
  url= "https://api.covid19india.org/data.json"
  page =requests.get(url)
  data = json.loads(page.text)
  lbl.configure(text="Total active cases:-"+data["statewise"][0]["active"])
  lbl2.configure(text="Page Refreshed")

btn = Button(window, text="Refresh", command=clicked)

btn.grid(column=3, row=0)

window.mainloop()