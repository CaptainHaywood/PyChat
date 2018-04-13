import shelve
import os

def topmenu():
    global motdN
    global motdA
    global motdB
    global motdC
    global motdD
    global motdE
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
    print ("--- JUPITER CHAT SERVER WIZARD ---")
    print ("")
    print ("1 Cosmetic Settings")
    print ("2 Functional Settings")
    print ("3 Save Changes and Quit")
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
            motdA = input("Line 1: ")
            motdB = input("Line 2: ")
            motdC = input("Line 3: ")
            motdD = input("Line 4: ")
            motdE = input("Line 5: ")
            topmenu()
        elif cosm == "2":
            print("--- NOTIFICATION TEXT ---")
            welcome = input("Welcome/Enter Handle Text: ")
            success = input("Successful Connection Text: ")
            topmenu()
        elif cosm == "3":
            topmenu()
        else:
            topmenu()
    elif top == "2":
        os.system('cls||echo -e \\\\033c')
        print ("--- FUNCTIONAL SETTINGS ---")
        print ("1 Server Name")
        print ("2 Connection Limit")
        print ("3 Logon Method")
        print ("4 Admin PIN")
        print ("5 Port")
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
            print("--- LOGON METHOD ---")
            print("The type of credentials required to login.")
            print("'Handle' logon requires only a username from the client and no other information. This method is best for casual chat rooms.")
            print("")
            print("'Account' logon requires a registered account (with a unique username and password) on the server. This may be set up when first connecting. This method is best for larger or more serious chat rooms, so as to prevent impersonation.")
            print("")
            print("1 'Handle' Logon")
            print("2 'Account' Logon")
            logonM = input("> ")
            topmenu()
        elif func == "4":
            os.system('cls||echo -e \\\\033c')
            print("--- ADMIN PIN ---")
            print("The Admin PIN is used differently depending on which logon method is used.")
            print("When using 'Handle' logon, users must type this PIN every time they want to use an administrative command.")
            print("")
            print("When using 'Account' logon, users can use the /verify command and enter this PIN to grant their accounts administrative priviledges that persist between commands and sessions.")
            adPIN = input("Enter PIN #: ")
            topmenu()
        elif func == "5":
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
        shelfFile['motdN_Var'] = motdN
        shelfFile['motdA_Var'] = motdA
        shelfFile['motdB_Var'] = motdB
        shelfFile['motdC_Var'] = motdC
        shelfFile['motdD_Var'] = motdD
        shelfFile['motdE_Var'] = motdE
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
    else:
        topmenu()
        


topmenu()
