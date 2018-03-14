import shelve
import os

def topmenu():
    print ("--- JUPITER CHAT SERVER WIZARD ---")
    print ("")
    print ("1 Cosmetic Settings")
    print ("2 Functional Settings")
    print ("3 Administration Settings")
    print ("4 Save Changes and Quit")
    print ("5 Quit Without Saving")
    top = input("> ")
    if top == "1":
        os.system('cls||echo -e \\\\033c')
        print ("--- COSMETIC SETTINGS ---")
        print ("")
        print ("1 Change MOTD")
        print ("2 Change Notification Text")
        print ("3 Return to Main Menu")
        cosm = input("> ")
        if cosm == "1":
            os.system('cls||echo -e \\\\033c')
            print("--- MOTD ---")
            print("The MOTD is five lines of text (plus a banner line) displayed to the user after a succesful connection.") 
            motdN = input("Banner Title: ")
            motd1 = input("Line 1: ")
            motd2 = input("Line 2: ")
            motd3 = input("Line 3: ")
            motd4 = input("Line 4: ")
            motd5 = input("Line 5: ")
            topmenu()
        elif cosm == "2":
            print("--- NOTIFICATION TEXT ---")
            welcome = input("Welcome/Enter Handle Text: ")
            success = input("Successful Connection Text: ")
            joined = input("Person Joined Text (assume name comes before this):")
            leaved = input("Person Left Text (assume name comes before this): ")
            topmenu()
        elif cosm == "3":
            topmenu()
    elif top == "2":
        os.system('cls||echo -e \\\\033c')
        print ("--- FUNCTIONAL SETTINGS ---")
        
        
        
                  
                  
        

topmenu()
