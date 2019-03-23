from cms import cms, options
from colorama import Fore

def menu(hospital, current_user):

    # Give the user some context.
    print(f"{Fore.MAGENTA}Available Options: ")

    # Set an initial value for choice other than the value for 'quit'.
    choice = ''

    # Start a loop that runs until the user enters the value for 'quit'.
    while choice != 'X':
        # Give all the choices in a series of print statements.
        if current_user.employee_type.lower() in ['medical', 'super admin']:
            print(
                f"\n{Fore.MAGENTA}Enter {Fore.WHITE}[1]{Fore.MAGENTA} to list all patients.")
            print(f"Enter {Fore.WHITE}[2]{Fore.MAGENTA} to add a patient.")
            print(f"Enter {Fore.WHITE}[3]{Fore.MAGENTA} to remove a patient.")
        if current_user.employee_type.lower() in ['medical', 'super admin', 'support']:
            print(
                f"Enter {Fore.WHITE}[4]{Fore.MAGENTA} to look up a patient record.")
        if current_user.employee_type.lower() in ['super admin']:
            print(
                f"Enter {Fore.WHITE}[5]{Fore.MAGENTA} to list all employees.")
            print(f"Enter {Fore.WHITE}[6]{Fore.MAGENTA} to add an employee.")
            print(
                f"Enter {Fore.WHITE}[7]{Fore.MAGENTA} to remove an employee.")
            print(
                f"Enter {Fore.WHITE}[8]{Fore.MAGENTA} to to look up an employee record.")
        print(
            f"Enter {Fore.WHITE}[9]{Fore.MAGENTA} to view your employee record.")
        print(f"Enter {Fore.WHITE}[X]{Fore.MAGENTA} to log out.")

        # Ask for the user's choice.
        choice = input(f"{Fore.MAGENTA}\nSelect >> {Fore.WHITE}")

        # Respond to the user's choice.
        if choice == '1' and current_user.employee_type.lower() in ['medical', 'super admin']:
            options.list_patients(hospital)
        elif choice == '2' and current_user.employee_type.lower() in ['medical', 'super admin']:
            options.add_patient(hospital)
        elif choice == '3' and current_user.employee_type.lower() in ['medical', 'super admin']:
            options.remove_patient(hospital)
        elif choice == '4' and current_user.employee_type.lower() in ['medical', 'super admin', 'support']:
            options.search_patient(hospital)
        elif choice == '5' and current_user.employee_type.lower() in ['super admin']:
            options.list_employees(hospital)
        elif choice == '6' and current_user.employee_type.lower() in ['super admin']:
            options.add_employee(hospital)
        elif choice == '7' and current_user.employee_type.lower() in ['super admin']:
            options.remove_employee(hospital)
        elif choice == '8' and current_user.employee_type.lower() in ['super admin']:
            options.search_employee(hospital)
        elif choice.upper() == '9':
            options.view_current_employee(hospital, current_user)
        elif choice.upper() == 'X':
            print("\nYou have logged off.\n")
            return
        else:
            print("\nI don't understand that choice, please try again.\n")

    # Print a message that we are all finished.
    print("Thanks again, bye now.")
