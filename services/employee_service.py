from typing import Optional

import database.db as mydb
import models.employee as employee
from rich.console import Console
from rich.table import Table

console = Console()


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
    table = Table("ID", "Name", "Age", "Address", "Role", "Project", "Salary", "Casual Leave",
                  "Sick Leave", "Joining Date", "Phone")
    for emp in res:
        table.add_row(
            str(emp.id),
            emp.name,
            str(emp.age),
            emp.address,
            emp.role,
            emp.project,
            str(emp.salary),
            str(emp.casual_leave),
            str(emp.sick_leave),
            emp.joining_date,
            emp.phone
        )
    console.print(table)
    #print(*res, sep='\n')


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

    if e_id is not None:
        query += " AND id = ?"
        params.append(e_id)
    if name is not None:
        query += " AND name = ?"
        params.append(name)
    if age is not None:
        query += " AND age = ?"
        params.append(age)
    if address is not None:
        query += " AND address = ?"
        params.append(address)
    if role is not None:
        query += " AND role = ?"
        params.append(role)
    if project is not None:
        query += " AND project = ?"
        params.append(project)
    if salary is not None:
        query += " AND salary = ?"
        params.append(salary)
    if casual_leave is not None:
        query += " AND casual_leave = ?"
        params.append(casual_leave)
    if sick_leave is not None:
        query += " AND sick_leave = ?"
        params.append(sick_leave)
    if joining_date is not None:
        query += " AND joining_date = ?"
        params.append(joining_date)
    if phone is not None:
        query += " AND phone = ?"
        params.append(phone)

    res = mydb.filter_employees(query, params)
    table = Table("ID", "Name", "Age", "Address", "Role", "Project", "Salary", "Casual Leave",
                  "Sick Leave", "Joining Date", "Phone")
    for emp in res:
        table.add_row(
            str(emp.id),
            emp.name,
            str(emp.age),
            emp.address,
            emp.role,
            emp.project,
            str(emp.salary),
            str(emp.casual_leave),
            str(emp.sick_leave),
            emp.joining_date,
            emp.phone
        )
    console.print(table)
