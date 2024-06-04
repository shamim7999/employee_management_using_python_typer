from typing import Optional

import typer
from services import employee_service as employee_service
from models import employee as employee

app = typer.Typer()


@app.command()
def add_employee(e_id: int, name: str, age: int, address: str, role: str, project: str,
                 salary: int, casual_leave: int, sick_leave: int, joining_date: str, phone: str):
    """Adds a new employee to the system.

    This function creates a new `Employee` object with the provided details and
    delegates adding the employee to the `employee_service`.

    Args:
        e_id (int): Unique employee ID.
        name (str): Employee's full name.
        age (int): Employee's age.
        address (str): Employee's residential address.
        role (str): Employee's job role within the company.
        project (str, optional): Project the employee is currently assigned to.
        salary (int): Employee's base salary.
        casual_leave (int): Number of casual leave days allotted to the employee.
        sick_leave (int): Number of sick leave days allotted to the employee.
        joining_date (str): Date the employee joined the company (YYYY-MM-DD format).
        phone (str): Employee's contact phone number.

    Returns:
        None
    """
    new_employee = employee.Employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave,
                                     joining_date, phone)
    employee_service.add_employee(new_employee)


@app.command()
def get_employee_by_id(e_id: int):
    """Retrieves an employee from the system by their ID.

    Args:
        e_id (int): Unique employee ID.

    Raises:
        Exception: If an error occurs while retrieving the employee.
    """
    employee_service.get_employee_by_id(e_id)


@app.command()
def delete_employee(e_id: int):
    """Deletes an employee from the system by their ID.

    Args:
        e_id (int): Unique employee ID.

    Raises:
        Exception: If an error occurs while deleting the employee.
    """
    employee_service.delete_employee_by_id(e_id)


@app.command()
def add_employees():
    """Adds a list of employees from the database.

    This function expects a list of employees stored in the `database.employee_data` module
    (replace with your actual implementation).

    Raises:
        Exception: If an error occurs while adding employees.
    """
    from database.employee_data import employees
    employee_service.add_employees(employees)


@app.command()
def show_employees():
    """Retrieves and displays all employees in the system.

     Raises:
         Exception: If an error occurs while retrieving employees.
     """
    employee_service.show_employees()


@app.command()
def increment_salary(e_id: int, percentage: float):
    """Increases an employee's salary by a given percentage.

    Args:
        e_id (int): Unique employee ID.
        percentage (float): Percentage increase for the salary (e.g., 0.1 for 10%).

    Raises:
        Exception: If an error occurs while updating the salary.
    """
    employee_service.increment_salary(e_id, percentage)


@app.command()
def change_project(e_id: int, project: str):
    """Updates an employee's assigned project.

    This function allows changing the project an employee is currently working on
    by specifying their ID and the new project name.

    Args:
        e_id (int): Unique employee ID.
        project (str): The new project name to assign to the employee.

    Raises:
        Exception: If an error occurs while updating the project.
    """
    employee_service.change_project(e_id, project)


@app.command()
def change_role(e_id: int, role: str):
    """Updates an employee's job role within the company.

    This function allows modifying an employee's job role by specifying their ID
    and the new role name.

    Args:
        e_id (int): Unique employee ID.
        role (str): The new job role for the employee.

    Raises:
        Exception: If an error occurs while updating the role.
    """
    employee_service.change_role(e_id, role)


@app.command()
def change_casual_leave(e_id: int, leave: int):
    """Updates the number of casual leave days for an employee.

    This function allows modifying the number of casual leave days allotted to an employee
    by specifying their ID and the new leave amount.

    Args:
        e_id (int): Unique employee ID.
        leave (int): The new number of casual leave days for the employee.

    Raises:
        Exception: If an error occurs while updating casual leave.
    """
    employee_service.change_casual_leave(e_id, leave)


@app.command()
def change_sick_leave(e_id: int, leave: int):
    """Updates the number of sick leave days for an employee.

    This function allows modifying the number of sick leave days allotted to an employee
    by specifying their ID and the new leave amount.

    Args:
        e_id (int): Unique employee ID.
        leave (int): The new number of sick leave days for the employee.

    Raises:
        Exception: If an error occurs while updating sick leave.
    """
    employee_service.change_sick_leave(e_id, leave)


@app.command()
def change_address(e_id: int, address: str):
    """Updates an employee's residential address.

    This function allows modifying an employee's residential address by specifying their ID
    and the new address.

    Args:
        e_id (int): Unique employee ID.
        address (str): The new residential address for the employee.

    Raises:
        Exception: If an error occurs while updating the address.
    """
    employee_service.change_address(e_id, address)


@app.command()
def change_phone(e_id: int, phone: str):
    """Updates an employee's contact phone number.

    This function allows modifying an employee's contact phone number by specifying their ID
    and the new phone number.

    Args:
        e_id (int): Unique employee ID.
        phone (str): The new contact phone number for the employee.

    Raises:
        Exception: If an error occurs while updating the phone number.
    """
    employee_service.change_phone(e_id, phone)


@app.command()
def total_working_year(e_id: int):
    """Calculates the total working years for an employee based on their joining date.

    This function retrieves the employee's joining date and calculates the total years
    they have been working with the company (up to the current date).

    Args:
        e_id (int): Unique employee ID.

    Raises:
        Exception: If an error occurs while retrieving the employee or calculating years.
    """
    employee_service.total_working_year(e_id)


@app.command()
def filter_employee(e_id: Optional[int] = None, name: Optional[str] = None, age: Optional[int] = None,
                    address: Optional[str] = None, role: Optional[str] = None, project: Optional[str] = None,
                    salary: Optional[int] = None, casual_leave: Optional[int] = None, sick_leave: Optional[int] = None,
                    joining_date: Optional[str] = None, phone: Optional[str] = None):
    """Filters and retrieves employees based on provided criteria.

    This function allows searching for employees by specifying optional parameters.
    It then delegates filtering the employees to the `employee_service`.

    Args:
        e_id (Optional[int]): Unique employee ID (optional).
        name (Optional[str]): Employee's full name (optional).
        age (Optional[int]): Employee's age (optional).
        address (Optional[str]): Employee's residential address (optional).
        role (Optional[str]): Employee's job role within the company (optional).
        project (Optional[str]): Project the employee is currently assigned to (optional).
        salary (Optional[int]): Employee's base salary (optional).
        casual_leave (Optional[int]): Number of casual leave days allotted to the employee (optional).
        sick_leave (Optional[int]): Number of sick leave days allotted to the employee (optional).
        joining_date (Optional[str]): Date the employee joined the company (YYYY-MM-DD format) (optional).
        phone (Optional[str]): Employee's contact phone number (optional).

    Returns:
        None
    """
    employee_service.filter_employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave,
                                     joining_date, phone)


employee_service.setup_database()

if __name__ == "__main__":
    app()
