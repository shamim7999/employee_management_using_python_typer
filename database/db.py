from datetime import datetime, timedelta
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

    cursor.execute('SELECT * FROM employee WHERE id = ?', (employee_id,))

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


def delete_employee_by_id(e_id):
    if get_employee(e_id) is None:
        print(not_found(e_id))
        return -1

    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employee WHERE id = ?", (e_id,))

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


def time_diff_test(e_id):
    if get_employee(e_id) is None:
        print(not_found(e_id))
        return
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    cursor.execute("SELECT joining_date FROM employee WHERE id = ?", (e_id,))
    result = cursor.fetchone()

    joining_date_str = result[0]
    joining_date = datetime.strptime(joining_date_str, '%Y-%m-%d')

    # Get the current date
    current_date = datetime.now()

    cursor.execute("SELECT timediff(datetime(?) , datetime(?, 'localtime')) as local_date",
                   (current_date, joining_date))

    row = cursor.fetchone()
    conn.close()

    if row:
        return employee.Employee(*row)
    else:
        return None


def total_working_year(e_id):
    if get_employee(e_id) is None:
        print(not_found(e_id))
        return -1
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    cursor.execute("""
            SELECT joining_date,
                   (julianday('now') - julianday(joining_date)) AS total_days
            FROM employee
            WHERE id = ?
        """, (e_id,))
    result = cursor.fetchone()

    if result is None:
        conn.close()
        return None

    joining_date_str, total_days = result
    total_days = int(total_days)

    # Calculate years, months, and days from total days
    years = total_days // 365
    remaining_days = total_days % 365
    months = remaining_days // 30
    days = remaining_days % 30

    # Close the database connection
    conn.close()
    if years < 0:
        years = 0
    # Return the result in the format yyyy:mm:dd
    return f" {years}Y:{months:02}M:{days:02}D"


def show_employees():
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employee')
    rows = cursor.fetchall()
    conn.close()
    return [employee.Employee(*row) for row in rows]


def increment_salary(e_id, percentage: float):
    if get_employee(e_id) is None:
        print(not_found(e_id))
        return
    the_employee = get_employee_by_id(e_id)
    the_employee.salary = the_employee.salary + (the_employee.salary * percentage / 100.0)
    update_employee(the_employee)
    msg(the_employee)


def change_project(e_id, project):
    if get_employee(e_id) is None:
        print(not_found(e_id))
        return -1
    the_employee = get_employee_by_id(e_id)
    the_employee.project = project
    update_employee(the_employee)
    msg(the_employee)


def change_phone(e_id, phone):
    if get_employee(e_id) is None:
        print(not_found(e_id))
        return -1
    the_employee = get_employee_by_id(e_id)
    the_employee.phone = phone
    update_employee(the_employee)
    msg(the_employee)


def change_casual_leave(e_id, leave):
    if get_employee(e_id) is None:
        print(not_found(e_id))
        return -1
    the_employee = get_employee_by_id(e_id)
    the_employee.casual_leave = leave
    update_employee(the_employee)
    msg(the_employee)


def change_sick_leave(e_id, leave):
    if get_employee(e_id) is None:
        print(not_found(e_id))
        return -1
    the_employee = get_employee_by_id(e_id)
    the_employee.sick_leave = leave
    update_employee(the_employee)
    msg(the_employee)


def change_role(e_id, role):
    if get_employee(e_id) is None:
        print(not_found(e_id))
        return -1
    the_employee = get_employee_by_id(e_id)
    the_employee.role = role
    update_employee(the_employee)
    msg(the_employee)


def change_address(e_id, address):
    if get_employee(e_id) is None:
        print(not_found(e_id))
        return -1
    the_employee = get_employee_by_id(e_id)
    the_employee.address = address
    update_employee(the_employee)
    msg(the_employee)


def msg(the_employee):
    print(f'Info of The updated Employee is: {the_employee}')
