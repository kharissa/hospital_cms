from cms import cms
import operator
import getpass
from colorama import Fore

def list_patients(hospital):
    for patient in hospital.patients:
        print(
            f"\n{Fore.MAGENTA}-------- PATIENT RECORD: {Fore.WHITE}{patient.patient_id} {Fore.MAGENTA}--------")
        print(f"{Fore.MAGENTA}Patient Name: {Fore.WHITE}{patient.name}")
        print(f"{Fore.MAGENTA}Description of Illness: {Fore.WHITE}{patient.illness}")


def add_patient(hospital):
    patient_name = input(f"Patient Name: ")
    patient_illness = input(f"Description of Illness: ")
    hospital.add_patient(cms.Patient(patient_name, patient_illness))


def remove_patient(hospital):
    patient_to_remove = input(f"To remove, input Patient ID: {Fore.WHITE}")
    
    if not any(patient.patient_id == patient_to_remove for patient in hospital.patients):
        print("Patient not found.")
    else:
        updated_patients = [patient for patient in hospital.patients if not patient.patient_id == patient_to_remove]
        hospital.patients = updated_patients
        print(f"Patient {patient_to_remove} was removed from the system.")


def search_patient(hospital):
    patient_lookup = input(
        f"{Fore.MAGENTA}To search, input Patient ID: {Fore.WHITE}")
    if not any(patient.patient_id == patient_lookup for patient in hospital.patients):
        print("Patient not found.")
    else:
        for patient in hospital.patients:
            if patient.patient_id == patient_lookup:
                print(
                    f"\n{Fore.MAGENTA}-------- PATIENT RECORD: {Fore.WHITE}{patient.patient_id} {Fore.MAGENTA}--------")
                print(f"{Fore.MAGENTA}Patient Name: {Fore.WHITE}{patient.name}")
                print(
                    f"{Fore.MAGENTA}Description of Illness: {Fore.WHITE}{patient.illness}")


def list_employees(hospital):
    for employee in hospital.employees:
        print(
            f"\n{Fore.MAGENTA}-------- EMPLOYEE RECORD: {Fore.WHITE}{employee.employee_id} {Fore.MAGENTA}--------")
        print(f"{Fore.MAGENTA}Employee Name: {Fore.WHITE}{employee.name}")
        print(f"{Fore.MAGENTA}Occupation: {Fore.WHITE}{employee.occupation}")


def add_employee(hospital):
    employee_name = input(f"Employee Name: ")
    employee_occupation = input(f"Occupation: ")
    employee_user_type = ""
    while employee_user_type.lower() not in ["super admin", "medical", "general", "support"]:
        employee_user_type = input(f"User Type [\"Super Admin\", \"Medical\", \"General\", \"Support\"]: ")
    employee_username = input(f"Username: ")
    employee_password = getpass.getpass(prompt="Password: ")
    hospital.add_employee(
        cms.Employee(employee_name, employee_occupation), employee_user_type, employee_username, employee_password)

def remove_employee(hospital):
    employee_to_remove = input(f"To remove, input Employee ID: {Fore.WHITE}")
    if not any(employee.employee_id == employee_to_remove for employee in hospital.employees):
        print("Employee not found.")
    else:
        updated_employees = [employee for employee in hospital.employees if not employee.employee_id == employee_to_remove]
        hospital.employees = updated_employees
        print(f"Employee {employee_to_remove} was removed from the system.")

def search_employee(hospital):
    employee_lookup = input(
        f"{Fore.MAGENTA}To search, input Employee ID: {Fore.WHITE}")
    if not any(employee.employee_id == employee_lookup for employee in hospital.employees):
        print("Employee not found.")
    else:
        for employee in hospital.employees:
            if employee.employee_id == employee_lookup:
                print(
                    f"\n{Fore.MAGENTA}-------- EMPLOYEE RECORD: {Fore.WHITE}{employee.employee_id} {Fore.MAGENTA}--------")
                print(f"{Fore.MAGENTA}Employee Name: {Fore.WHITE}{employee.name}")
                print(
                    f"{Fore.MAGENTA}Occupation: {Fore.WHITE}{employee.occupation}")

def view_current_employee(hospital, current_user):
    for employee in hospital.employees:
        if employee.employee_id == current_user.employee_id:
            print(
                f"\n{Fore.MAGENTA}-------- EMPLOYEE RECORD: {Fore.WHITE}{employee.employee_id} {Fore.MAGENTA}--------")
            print(f"{Fore.MAGENTA}Employee Name: {Fore.WHITE}{employee.name}")
            print(f"{Fore.MAGENTA}Occupation: {Fore.WHITE}{employee.occupation}")
