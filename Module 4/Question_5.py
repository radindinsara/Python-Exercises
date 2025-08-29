real_username = "python"
real_passcode = "rules"
login_attempt = 0
entry_time = 5

while login_attempt < entry_time :
    user_name = input("Enter username: ")
    user_psw = input("Enter password: ")

    if user_name == real_username and user_psw == real_passcode:
        print("Welcome")
        break
    else:
        login_attempt += 1
        if login_attempt == entry_time:
            print("Access denied")     
            break
        else:
            print("Incorrect username or password. Please try again.")