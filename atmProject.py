# IMPORTS
import random
import datetime

# DATABASE
user_database = {1111111111: ['Soph', 'Velasquez', 'soph@email.com', 'pwSoph'],
                 2222222222: ["Jazz", "Jazz", "jazz@email.com", "pwJazz"],
                 3333333333: ["Jo", "Jo", "jojo@email.com", "pwJojo"]}


# INITIALIZING THE SYSTEM // DEFINING FUNCTIONS

def init():
    print('*****ʕ·͡ᴥ·ʔ Welcome to bank Sophos. ʕ·͡ᴥ·ʔ*****')
    have_account = int(input('Do you have an account with us? \n 1 (Yes) \n 2 (No)\n'))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print('Invalid option selected.')
        init()


def register():
    print("***** Register *****")

    email = input("What is your email address?\n")
    firstname = input("What is your first name?\n")
    lastname = input("What is your last name?\n")
    password = input("Create a password for yourself:\n")

    account_number = generate_account_number()

    user_database[account_number] = [email, firstname, lastname, password]

    print("Account created.\nYour account number is: %d.\nPlease log in using your new credentials." % account_number)

    init()


def login():
    flag = 0
    attempted_account_number = int(input("\nWhat is your account number?\n"))
    attempted_password = input("\nWhat is your password?\n")

    for account_number, user_details in user_database.items():
        if account_number == attempted_account_number and user_details[3] == attempted_password:
            flag = 1
            print("ʕっ•ᴥ•ʔっ Login successful! ʕっ•ᴥ•ʔっ")
            bank_operation(user_details)
    if flag == 0:
        print("Invalid account or password.")
        try_again = int(input("Try again?\n(1) Yes\n(2) No\n"))
        if try_again == 1:
            login()
        else:
            print("Exiting.\n")
            exit()


def bank_operation(user):
    now = datetime.datetime.now()
    print("Welcome %s %s." % (user[0], user[1]))
    print("The time is:")
    print(now.strftime("%m-%d-%y, %H:%M:%S"))
    selected_option = int(input("What would you like to do?\n(1) Deposit\n(2) Withdrawal\n(3) Log out\n(4) Exit\n"))

    if selected_option == 1:
        deposit_operation()
        make_another_trans = int(input("Make another transaction?\n(1) Yes\n(2) No\n"))
        if make_another_trans == 1:
            bank_operation(user)
        elif make_another_trans == 2:
            print("Have a nice day!")
            exit()

    elif selected_option == 2:
        withdrawal_operation()
        make_another_trans = int(input("Make another transaction?\n(1) Yes\n(2) No\n"))
        if make_another_trans == 1:
            bank_operation(user)
        elif make_another_trans == 2:
            print("Have a nice day!")
            exit()

    elif selected_option == 3:
        print('Logging Out...')
        print('You are now logged out. Redirecting to home page.')
        init()

    elif selected_option == 4:
        print("Have a nice day!")
        exit()

    else:
        print("Invalid option selected.")
        bank_operation(user)


def withdrawal_operation():
    print("This is the withdrawal page.")
    withdraw_amount = int(input("How much would you like to withdraw?"))
    print("Please take your $%s." % withdraw_amount)


def deposit_operation():
    print("This is the deposit page.")
    deposit_amount = int(input("How much would you like to deposit?"))
    print("Depositing $%s." % deposit_amount)


def generate_account_number():
    return random.randrange(1000000000, 9999999999)


# ACTUAL BANKING SYSTEM
init()