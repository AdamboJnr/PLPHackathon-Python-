import datetime
#Set the password
password = "Password123"

#Set the commands to instruct door
open_door = "Open"
close_door = "Close"

#Flag to help stop the program
active = True

while active:
    option = input("\nInput an option\n1.Open\n2.Close\n3.quit\n")

    #Quitting the program    
    if option == "quit":
        active = False

    elif option == open_door:  #Condition to check if door is opened

        inp_password = input("Key in Password:")
    
        if inp_password == password:   #Comapring if password matches     
            print("\nThe door is now open")
            time_open = datetime.datetime.now()
            print("Door last opened at " + str(time_open))

            #Checking if door is already open
            option2 = input("\nInput an option\n1.Open\n2.Close\n3.quit\n")

            if option2 == open_door:
                print("Door Already open")
                print("Door last opened at " + str(time_open))
            elif option2 == close_door:
                print("\nThe door is now closed")
                time_closed = datetime.datetime.now()
                print("Door last closed at " + str(time_closed))
            elif option2 == "quit":
                active = False
            else:
                print("\nChoose valid option")
        else:   # Inform user of Wrong password 
            print("Wrong Password!! Please try again")

    elif option == close_door: #Condition to Check if user closes door
        print("\nThe door is now Closed")
        time_closed = datetime.datetime.now()
        print("Door last closed at " + str(time_closed))

        # Check if door is already closed
        option2 = input("\nInput an option\n1.Open\n2.Close\n3.quit\n")
        
        if option2 == open_door:
            print("\nThe door is now open")
            time_open = datetime.datetime.now()
            print("Door last opened at " + str(time_open))

        elif option2 == close_door:
            print("\nThe door is already closed")
            time_closed = datetime.datetime.now()
            print("Door last closed at " + str(time_closed))

        elif option2 == "quit":
            active = False

        else:
            print("\nChoose a valid option")

    # If option entered is not recognized
    else:       
        print("\nChoose a valid option")

        

