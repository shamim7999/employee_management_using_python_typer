import sqlite3
import models.employee as employee


def setup_database():
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            address TEXT NOT NULL,
            role TEXT NOT NULL,
            project TEXT NOT NULL,
            salary INTEGER,
            casual_leave INTEGER,
            sick_leave INTEGER,
            joining_date TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def get_employee(employee_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM employee WHERE id = ?', (employee_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return employee.Employee(*row)
    else:
        return None


def not_found(employee_id):
    return f"Not found Employee with ID: {employee_id}"


def found(employee_id):
    return f"Employee with ID: {employee_id} is already in database."


def add_employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave, joining_date, phone):
    if get_employee(e_id) is not None:
        print(found(e_id))
        return

    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    new_employee = employee.Employee(e_id, name, age, address, role, project, salary, casual_leave, sick_leave,
                                     joining_date, phone)

    cursor.execute('INSERT INTO employee (id, name, age, address, role, project, salary, casual_leave, '
                   'sick_leave, joining_date, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (new_employee.id, new_employee.name, new_employee.age, new_employee.address,
                    new_employee.role, new_employee.project, new_employee.salary, new_employee.casual_leave,
                    new_employee.sick_leave, new_employee.joining_date, new_employee.phone))

    print(f'Added person: {new_employee}')

    conn.commit()
    conn.close()


def update_employee(new_employee):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE employee
        SET name = ?, age = ?, address = ?, role = ?, project = ?, salary = ?, casual_leave = ?, 
            sick_leave = ?, joining_date = ?, phone = ?
        WHERE id = ?
    ''', (new_employee.name, new_employee.age, new_employee.address, new_employee.role,
          new_employee.project, new_employee.salary, new_employee.casual_leave,
          new_employee.sick_leave, new_employee.joining_date, new_employee.phone,
          new_employee.id))

    conn.commit()
    conn.close()


def save_employee(new_employee: employee):
    add_employee(new_employee.id, new_employee.name, new_employee.age, new_employee.address,
                 new_employee.role, new_employee.project, new_employee.salary, new_employee.casual_leave,
                 new_employee.sick_leave, new_employee.joining_date, new_employee.phone)


def get_employee_by_id(e_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM employee WHERE id=?', (e_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return employee.Employee(*row)
    else:
        return None


def show_employees():
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employee')
    rows = cursor.fetchall()
    conn.close()
    return [employee.Employee(*row) for row in rows]


def increment_salary(e_id, percentage: float):
    the_employee = get_employee_by_id(e_id)
    the_employee.salary = the_employee.salary + (the_employee.salary * percentage / 100.0)
    update_employee(the_employee)
    print(f'The Employee is: {the_employee}')
