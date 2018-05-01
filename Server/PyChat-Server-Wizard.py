import shelve
import os

shelfFile = shelve.open('server_config')
welcome = shelfFile['welcome_Var']
success = shelfFile['success_Var']
servername = shelfFile['servername_Var']
maxconn = shelfFile['maxconn_Var']
logonM = shelfFile['logonM_Var']
adPIN = shelfFile['adPIN_Var']
sport = shelfFile['sport_Var']
shelfFile.close()

def topmenu():
    global welcome
    global success
    global joined
    global leaved
    global servername
    global maxconn
    global logonM
    global adPIN
    global sport
    os.system('cls||echo -e \\\\033c')
    print ("--- PYCHAT SERVER WIZARD ---")
    print ("")
    print ("1 Cosmetic Settings")
    print ("2 Functional Settings")
    print ("3 Save Changes and Quit")
    top = input("> ")
    if top == "1":
        os.system('cls||echo -e \\\\033c')
        print ("--- COSMETIC SETTINGS ---")
        print ("")
        print ("1 Change Notification Text")
        print ("2 Return to Main Menu")
        cosm = input("> ")
        if cosm == "1":
            print("--- NOTIFICATION TEXT ---")
            welcome = input("Welcome/Enter Handle Text: ")
            success = input("Successful Connection Text: ")
            topmenu()
        elif cosm == "2":
            topmenu()
        else:
            topmenu()
    elif top == "2":
        os.system('cls||echo -e \\\\033c')
        print ("--- FUNCTIONAL SETTINGS ---")
        print ("1 Server Name")
        print ("2 Connection Limit")
        print ("3 Admin PIN")
        print ("4 Port")
        print ("5 Return to Main Menu")
        func = input("> ")
        if func == "1":
            os.system('cls||echo -e \\\\033c')
            print ("--- SERVER NAME ---")
            servername = input("Enter Name: ")
            topmenu()
        elif func == "2":
            os.system('cls||echo -e \\\\033c')
            print("--- CONNECTION LIMIT ---")
            print("The maximum number of clients that can be connected at any time.")
            maxconn = input("Enter #:")
            maxconn = int(maxconn)
            topmenu()
        elif func == "3":
            os.system('cls||echo -e \\\\033c')
            print("--- ADMIN PIN ---")
            print("Users must type this PIN every time they want to use an administrative command.")
            adPIN = input("Enter PIN #: ")
            topmenu()
        elif func == "4":
            print("--- PORT ---")
            print("The port is a number value that signifies which virtual 'port' the chat traffic is flowing through to get to your computer and out to the Internet. This number is required to connect properly, and is set to 33000 by default.")
            sport = input("Enter a Port # (1-65535): ")
            sport = int(sport)
            if sport > 0 and sport < 65536:
                topmenu()
            else:
                print("Invalid Port #! Please re-try.")
                sport = 33000
                wait = input("Press enter to continue.")
                topmenu()
        else:
            topmenu()
    elif top == "3":
        os.system('cls||echo -e \\\\033c')
        print("Saving settings...")
        shelfFile = shelve.open('server_config')
        shelfFile['welcome_Var'] = welcome
        shelfFile['success_Var'] = success
        shelfFile['servername_Var'] = servername
        shelfFile['maxconn_Var'] = maxconn
        shelfFile['logonM_Var'] = logonM
        shelfFile['adPIN_Var'] = adPIN
        shelfFile['sport_Var'] = sport
        shelfFile.close()
        print("Settings saved! It is now safe to exit the wizard. Pressing enter will bring you back to the main menu.")
        wait = input("Press enter to return to main menu.")
        topmenu()
    else:
        topmenu()
        


topmenu()
