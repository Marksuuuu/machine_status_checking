from datetime import datetime
choice = ''
time_stamp = datetime.now()
time_stamp1 = datetime.now()
started = time_stamp.strftime("%d/%m/%Y %H:%M:%S")
started_1 = time_stamp1.strftime("%d/%m/%Y %H:%M:%S")

f = open("date_data.txt", "a")
f.write("IDLE TIME: " + (started) + '\n')
f.write('----------------------------------------\n')
f.close()
while choice != 'EXIT':
    print("\n[1] START")
    print("[2] RUNNING / ON PRODUCTION")
    print("[3] DOWN UNAVAILABLE")
    print("[EXIT] Enter EXIT to exit.")


    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")
    
   
    # Respond to the user's choice.
    if choice == '1':
        print("\nMachine Started!\n")
        f = open("date_data.txt", "a")
        f.write('MACHINE STARTED: ' + (started_1) + '\n')
        f.write('----------------------------------------\n')
        f.close()
        message='Machine Started!'

    elif choice == '2':
        print("\nMachine are Running!\n")
        f = open("date_data.txt", "a")
        f.write('MACHINE RUNNING: ' + (started) + '\n')
        f.write('----------------------------------------\n')
        f.close()
    elif choice == '3':
        print("\nMachine are Unavailable!\n")
        f = open("date_data.txt", "a")
        f.write('MACHINE UNAVAILABLE: ' + (started) + '\n')
        f.write('----------------------------------------\n')
        f.close()
    elif choice == 'EXIT':
        print("\nMachine STOP!!\n")
        f = open("date_data.txt", "a")
        f.write('MACHINE STOP: ' + (started) + '\n')
        f.write('----------------------------------------\n')
        f.close()
    else:
        print("\nI don't understand that choice, please try again.\n")
        
# Print a message that we are all finished.
print("Thanks again, bye now.")