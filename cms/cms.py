import random
import string

class Hospital():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = []
        self.patients = []
        self.records = []

    def add_patient(self, patient):
        patient.patient_id = self.create_id()
        self.patients.append(patient)

    def add_employee(self, employee, user_type, username, password):
        employee.employee_id = self.create_id()
        employee.employee_type = user_type
        employee.username = username
        employee.password = password
        self.employees.append(employee)

    def create_id(id_type):
        return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(4)])


class Patient():
    def __init__(self, name, illness):
        self.name = name
        self.illness = illness


class Employee():
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
