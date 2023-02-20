import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter.messagebox import showinfo



# root window
root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('TIME CAPTURE HERE')

time_stamp = datetime.now()
started = time_stamp.strftime("%d/%m/%Y %H:%M:%S")
f = open("date_data.txt", "a")
f.write('MACHINE IDLE: ' + (started) + '\n')
f.write('----------------------------------------\n')
f.close()


def main():
   if text == 'START':
      print('here')
   elif text == 'RUNNING / ON PRODUCTION':
      print('asd')
   else:
      print('asd')


# def machine_started():
#    time_stamp = datetime.now()
#    started = time_stamp.strftime("%d/%m/%Y %H:%M:%S")
#    f = open("date_data.txt", "a")
#    f.write('MACHINE STARTED: ' + (started) + '\n')
#    f.write('----------------------------------------\n')
#    f.close()
#    showinfo(
#         title='MACHINE STARTED',
#         message='MACHINE STARTED!'
#    )
# def machine_run():
#    time_stamp = datetime.now()
#    started = time_stamp.strftime("%d/%m/%Y %H:%M:%S")
#    f = open("date_data.txt", "a")
#    f.write('MACHINE RUNNING: ' + (started) + '\n')
#    f.write('----------------------------------------\n')
#    f.close()
#    showinfo(
#         title='MACHINE RUNNING',
#         message='MACHINE RUNNING!'
#    )
# def machine_stop():
#    time_stamp = datetime.now()
#    started = time_stamp.strftime("%d/%m/%Y %H:%M:%S")
#    f = open("date_data.txt", "a")
#    f.write('MACHINE UNAVAILABLE: ' + (started) + '\n')
#    f.write('----------------------------------------\n')
#    f.close()
#    showinfo(
#         title='MACHINE UNAVAILABLE',
#         message='MACHINE UNAVAILABLE!'
#    )
# def machine_exit():
#    time_stamp = datetime.now()
#    started = time_stamp.strftime("%d/%m/%Y %H:%M:%S")
#    f = open("date_data.txt", "a")
#    f.write('MACHINE STOP: ' + (started) + '\n')
#    f.write('----------------------------------------\n')
#    f.close()
#    showinfo(
#         title='EXIT',
#         message='BYE!'
#    )
#    root.quit()


# exit button


start_button = ttk.Button(
    root,
    text='START',
    command=main
)

start_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)

run_button = ttk.Button(
    root,
    text='RUNNING / ON PRODUCTION',
    command=main
)
run_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)
stop_button = ttk.Button(
    root,
    text='DOWN UNAVAILABLE',
    command=main
)
stop_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)

exit_button = ttk.Button(
    root,
    text='EXIT',
    command=main
)

exit_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)

root.mainloop()