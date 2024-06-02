import typer
import services.employee_service as em_serv

app = typer.Typer()


@app.command()
def just_test(item: str):
    print(f"Creating item: {item}")


@app.command()
def add_employee(e_id: int, name: str, age: int, address: str, role: str, project: str,
                 salary: int, casual_leave: int, sick_leave: int, joining_date: str, phone: str):
    em_serv.add_employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave,
                         joining_date, phone)


@app.command()
def show_employees():
    em_serv.show_employees()


@app.command()
def increment_salary(e_id: int, percentage: float):
    em_serv.increment_salary(e_id, percentage)


em_serv.setup_database()

if __name__ == "__main__":
    app()
