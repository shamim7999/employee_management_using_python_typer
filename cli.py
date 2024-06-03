from typing import Optional

import typer
import services.employee_service as em_serv

app = typer.Typer()


@app.command()
def add_employee(e_id: int, name: str, age: int, address: str, role: str, project: str,
                 salary: int, casual_leave: int, sick_leave: int, joining_date: str, phone: str):
    em_serv.add_employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave,
                         joining_date, phone)


@app.command()
def get_employee_by_id(e_id: int):
    em_serv.get_employee_by_id(e_id)


@app.command()
def delete_employee(e_id: int):
    em_serv.delete_employee_by_id(e_id)


@app.command()
def add_employees():
    from database.employee_data import employees
    em_serv.add_employees(employees)


@app.command()
def show_employees():
    em_serv.show_employees()


@app.command()
def increment_salary(e_id: int, percentage: float):
    em_serv.increment_salary(e_id, percentage)


@app.command()
def change_project(e_id: int, project: str):
    em_serv.change_project(e_id, project)


@app.command()
def change_role(e_id: int, role: str):
    em_serv.change_role(e_id, role)


@app.command()
def change_casual_leave(e_id: int, leave: int):
    em_serv.change_casual_leave(e_id, leave)


@app.command()
def change_sick_leave(e_id: int, leave: int):
    em_serv.change_sick_leave(e_id, leave)


@app.command()
def change_address(e_id: int, address: str):
    em_serv.change_address(e_id, address)


@app.command()
def change_phone(e_id: int, phone: str):
    em_serv.change_phone(e_id, phone)


@app.command()
def total_working_year(e_id: int):
    em_serv.total_working_year(e_id)


@app.command()
def filter_employee(e_id: Optional[int] = None, name: Optional[str] = None, age: Optional[int] = None,
                    address: Optional[str] = None, role: Optional[str] = None, project: Optional[str] = None,
                    salary: Optional[int] = None, casual_leave: Optional[int] = None, sick_leave: Optional[int] = None,
                    joining_date: Optional[str] = None, phone: Optional[str] = None):
    em_serv.filter_employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave, joining_date,
                            phone)


em_serv.setup_database()

if __name__ == "__main__":
    app()
