import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter.constants import DISABLED, NORMAL
from tkinter.messagebox import showinfo
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="machine_sample"
)

my_cursor = mydb.cursor()


# root window
root = tk.Tk()
root.geometry('900x300')
root.resizable(False, False)
root.title('TIME CAPTURE HERE')
title_idle = 'IDLE'
time_stamp = datetime.now()
started = time_stamp.strftime("%Y-%m-%d %H:%M:%S.%f")
print(started)
query = "INSERT INTO date_time_capture (status,date_time) VALUES (%s, %s)"
values = (title_idle,started)
my_cursor.execute(query,values)
mydb.commit()


def machine_started():
   downtime_button['state'] = DISABLED
   title_idle = 'STARTED'
   time_stamp = datetime.now()
   started = time_stamp.strftime("%Y-%m-%d %H:%M:%S.%f")
   print(started)
   label_here.config(text = title_idle + ' AT: ' + ' '+ started)
   query = "INSERT INTO date_time_capture (status,date_time) VALUES (%s, %s)"
   values = (title_idle,started)
   my_cursor.execute(query,values)
   mydb.commit()


def machine_run():
   start_button['state'] = DISABLED
   title_idle = 'IN PRODUCTION'
   time_stamp = datetime.now()
   started = time_stamp.strftime("%Y-%m-%d %H:%M:%S.%f")
   label_here.config(text = title_idle + ' AT: ' + ' '+ started)
   print(started)
   # query = "INSERT INTO date_time_capture (status,date_time) VALUES (%s, %s)"
   # values = (title_idle,started)
   # my_cursor.execute(query,values)
   # mydb.commit()


   downtime_button['state'] = NORMAL


def machine_stop():
   title_idle = 'MACHINE DOWNTIME'
   time_stamp = datetime.now()
   started = time_stamp.strftime("%Y-%m-%d %H:%M:%S.%f")
   print(started)
   label_here.config(text = title_idle + ' AT: ' + ' '+ started)
   query = "INSERT INTO date_time_capture (status,date_time) VALUES (%s, %s)"
   values = (title_idle,started)
   my_cursor.execute(query,values)
   mydb.commit()
 

def machine_idle():
   downtime_button['state'] = DISABLED
   title_idle = 'IDLE'
   time_stamp = datetime.now()
   started = time_stamp.strftime("%Y-%m-%d %H:%M:%S.%f")
   print(started)
   query = "INSERT INTO date_time_capture (status,date_time) VALUES (%s, %s)"
   values = (title_idle,started)
   my_cursor.execute(query,values)
   mydb.commit()
 
   showinfo(
        title='MACHINE IDLE',
        message='MACHINE IDLE!: ' + started,
   )

def machine_exit():
   time_stamp = datetime.now()
   started = time_stamp.strftime("%d/%m/%Y %H:%M:%S")

   showinfo(
        title='EXIT',
        message='BYE!'
   )
   root.quit()

# exit button

start_button = ttk.Button(
    root,
    text='START',
    width=40,
    command = machine_started
)

start_button.pack(
    expand=True
)
start_button.place(
    x=30,
    y=30,
   )

production_button = ttk.Button(
    root,
    text='PRODUCTION',
    command=machine_run,
    width=40
)
production_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)

production_button.place(
    x=30,
    y=70,
)

downtime_button = ttk.Button(
    root,
    text='DOWNTIME',
    command=machine_stop,
    state = NORMAL,
    width = 40
)
downtime_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)
downtime_button.place(
    x=30,
    y=110,
)

label_here1 = ttk.Label(
    root,
    text='STATUS : ',
    font = ("Courier Prime", 13 )
)
label_here1.place(
    x=350,
    y=30,
)

label_here = ttk.Label(
    root,
    text='',
    font = ("Courier Prime", 13 )
)
label_here.place(
    x=450,
    y=30,
)


root.mainloop()