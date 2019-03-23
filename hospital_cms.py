import getpass
from cms import cms, menu
from colorama import Fore

def cms_init(hospital):
    print(Fore.MAGENTA + "===========================================")
    print(f"  {Fore.WHITE}{hospital.name}")
    print(Fore.MAGENTA + "===========================================")
    user = input(f"{Fore.MAGENTA}Please enter your username: {Fore.WHITE}")
    password = getpass.getpass(
        prompt=f"{Fore.MAGENTA}Please enter your password: ")
    print(Fore.MAGENTA + "-------------------------------------------")

    current_user = ""

    for employee in hospital.employees:
        if employee.username == user and employee.password == password:
            current_user = employee
            print(
                f"{Fore.MAGENTA}Welcome, {Fore.WHITE}{employee.name}\n{Fore.MAGENTA}Your access level is: {Fore.WHITE}{employee.employee_type.upper()}")
            break

    if not current_user:
        print(f"{Fore.WHITE}Your username and/or password does not match our records.")
        return
    print(Fore.MAGENTA + "-------------------------------------------")
    menu.menu(hospital, current_user)


#######################     DRIVER_CODE     #######################

# Create sick persons
chi_park = cms.Patient("Charlyne Yi", "Neverending hiccups")
jessica_adams = cms.Patient("Jessica Adams", "Skin rash on back")
martha_masters = cms.Patient("Martha Masters", "Dizzy spells in the morning")

# Create job-seekers
gregory_house = cms.Employee(
    "Dr. Gregory House", "Head of Department of Diagnostic Medicine")
lisa_cuddy = cms.Employee("Dr. Lisa Cuddy", "Dean of Medicine")
james_wilson = cms.Employee("James Wilson", "Front Desk Receptionist")
eric_foreman = cms.Employee("Eric Foreman", "Facilities - Janitorial")

# Create hospital
princeton = cms.Hospital(
    "Princeton–Plainsboro Teaching Hospital", "New Jersey")

# Add employees to hospital
princeton.add_employee(gregory_house, "medical", "house", "house")
princeton.add_employee(lisa_cuddy, "super admin", "cuddy", "cuddy")
princeton.add_employee(james_wilson, "support", "wilson", "wilson")
princeton.add_employee(eric_foreman, "general", "foreman", "foreman")

# Add patients to hospital
princeton.add_patient(chi_park)
princeton.add_patient(jessica_adams)
princeton.add_patient(martha_masters)

# Initialize Hospital CMS
cms_init(princeton)
