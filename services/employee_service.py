import database.db as mydb
import models.employee as employee


def setup_database():
    mydb.setup_database()


def add_employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave, joining_date, phone):
    new_employee = employee.Employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave,
                                     joining_date, phone)
    mydb.save_employee(new_employee)


def show_employees():
    print(*mydb.show_employees(), sep='\n')


def increment_salary(e_id, percentage: float):
    mydb.increment_salary(e_id, percentage)
