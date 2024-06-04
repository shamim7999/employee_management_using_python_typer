from typing import Optional

import database.db as mydb
import models.employee as employee
from rich.console import Console
from rich.table import Table

console = Console()


def setup_database():
    mydb.setup_database()


def add_employee(new_employee):
    mydb.add_employee(new_employee)


def add_employees(employees):
    for the_employee in employees:
        new_employee = employee.Employee(*the_employee)
        mydb.add_employee(new_employee)


def show_employees():
    res = mydb.show_employees()
    if len(res) == 0:
        print('No Data Found.')
        return
    table = Table("ID", "Name", "Age", "Address", "Role", "Project", "Salary", "Casual Leave",
                  "Sick Leave", "Joining Date", "Phone")
    for the_employee in res:
        table.add_row(
            str(the_employee.id),
            the_employee.name,
            str(the_employee.age),
            the_employee.address,
            the_employee.role,
            the_employee.project,
            str(the_employee.salary),
            str(the_employee.casual_leave),
            str(the_employee.sick_leave),
            the_employee.joining_date,
            the_employee.phone
        )
    console.print(table)


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


def get_employee_by_id(e_id):
    res = mydb.get_employee_by_id(e_id)
    if res is None:
        print(mydb.not_found(e_id))
        return
    print(res)


def filter_employee(e_id: Optional[int], name: Optional[str], age: Optional[int], address: Optional[str],
                    role: Optional[str], project: Optional[str], salary: Optional[int], casual_leave: Optional[int],
                    sick_leave: Optional[int], joining_date: Optional[str], phone: Optional[str]):
    query = "SELECT * FROM employee WHERE 1=1"
    params = []

    conditions = {
        "id": e_id,
        "name": name,
        "age": age,
        "address": address,
        "role": role,
        "project": project,
        "salary": salary,
        "casual_leave": casual_leave,
        "sick_leave": sick_leave,
        "joining_date": joining_date,
        "phone": phone
    }

    for key, value in conditions.items():
        if value is not None:
            params.append(value)
            query += f' AND {key}=?'

    res = mydb.filter_employees(query, params)
    table = Table("ID", "Name", "Age", "Address", "Role", "Project", "Salary", "Casual Leave",
                  "Sick Leave", "Joining Date", "Phone")
    for the_employee in res:
        table.add_row(
            str(the_employee.id),
            the_employee.name,
            str(the_employee.age),
            the_employee.address,
            the_employee.role,
            the_employee.project,
            str(the_employee.salary),
            str(the_employee.casual_leave),
            str(the_employee.sick_leave),
            the_employee.joining_date,
            the_employee.phone
        )
    console.print(table)
