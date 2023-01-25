class Employee:

    raise_amt = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + '.' + lastname + '@email.com'
        self.pay = pay

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, firstname, lastname, pay, prog_lang):
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, firstname, lastname, pay, employees=None):
        super().__init__(firstname, lastname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())


developer_1 = Developer('Tony', 'Ingerlund', 45000, 'Javascript')
developer_2 = Developer('Mase', 'Rogers', 34000, 'Java')
manager_1 = Manager('Barbara', "Boyle", 80000, [developer_1])


print(developer_1.pay)
print(manager_1.email)

manager_1.add_employee(developer_2)
manager_1.remove_employee(developer_1)

manager_1.print_employees()
