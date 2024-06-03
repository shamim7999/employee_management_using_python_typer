import database.db as mydb
import models.employee as employee


def setup_database():
    mydb.setup_database()


def add_employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave, joining_date, phone):
    new_employee = employee.Employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave,
                                     joining_date, phone)
    mydb.save_employee(new_employee)


def add_employees(employees):
    for emp in employees:
        new_employee = employee.Employee(*emp)
        mydb.save_employee(new_employee)


def show_employees():
    res = mydb.show_employees()
    if len(res) == 0:
        print('No Data Found.')
        return
    print(*res, sep='\n')


def increment_salary(e_id, percentage: float):
    mydb.increment_salary(e_id, percentage)


def total_working_year(e_id):
    res = mydb.total_working_year(e_id)
    if res == -1:
        return
    print(f'Total Experience for ID: {e_id} is {res}')


def time_diff_test(e_id):
    print(f'Time Diff: {mydb.time_diff_test(e_id)}')


def delete_employee_by_id(e_id):
    if mydb.delete_employee_by_id(e_id) == -1:
        return
    print(f'Employee with ID: {e_id} Deleted.')


def change_project(e_id, project):
    if mydb.change_project(e_id, project) == -1:
        return
    print(f'Project Changed for ID: {e_id}')


def change_role(e_id, role):
    if mydb.change_role(e_id, role) == -1:
        return
    print(f'Role Changed for ID: {e_id}')


def change_address(e_id, address):
    if mydb.change_address(e_id, address) == -1:
        return
    print(f'Address Changed for ID: {e_id}')


def change_casual_leave(e_id, leave):
    if mydb.change_casual_leave(e_id, leave) == -1:
        return
    print(f'Casual Leave Changed for ID: {e_id}')


def change_sick_leave(e_id, leave):
    if mydb.change_sick_leave(e_id, leave) == -1:
        return
    print(f'Sick Leave Changed for ID: {e_id}')


def change_phone(e_id, phone):
    if mydb.change_phone(e_id, phone) == -1:
        return
    print(f'Phone Number Changed for ID: {e_id}')
