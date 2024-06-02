class Employee:
    def __init__(self, e_id, name, age, address, role, project, salary, casual_leave, sick_leave, joining_date, phone):
        self.id = e_id
        self.name = name
        self.age = age
        self.address = address
        self.role = role
        self.project = project
        self.salary = salary
        self.casual_leave = casual_leave
        self.sick_leave = sick_leave
        self.joining_date = joining_date
        self.phone = phone

    def __str__(self):
        return (f"Employee(id={self.id}, name={self.name}, age={self.age}, address={self.address}, "
                f"role={self.role}, project={self.project}, "
                f"salary={self.salary}, "
                f"casual_leave={self.casual_leave}, sick_leave={self.sick_leave}, "
                f"joining_date={self.joining_date}, phone={self.phone})")
