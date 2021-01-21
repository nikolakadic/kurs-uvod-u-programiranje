"""
Continue OO exercise
"""


class Employee:
    """
    Class that represents our employee.
    """

    def __init__(self, employee_id, ssid, name, surname, salary):
        self._employee_id = employee_id
        self.__ssid = ssid
        self.name = name
        self.surname = surname
        self.salary = salary

    def __str__(self):
        return f"{self.name} - {self.surname}"

    def __repr__(self):
        return f"{self.name} - {self.surname}"

    def __eq__(self, comparing_employee):
        return self.__ssid == comparing_employee.__ssid

    def __add__(self, another_employee):
        return self.salary + another_employee.salary


john = Employee(5, 20202002020, "John", "Doe", 200)
sara = Employee(6, 20202002020, "Sara", "Doe", 200)

# marko = john + sara
# together_salaries = john == sara

print(john)
# print(together_salaries)

# print(john._Employee__ssid)

# print(dir(john))

# public  // private // protected -- [vidjljivost atributa/metoda van klase]
# overriding operatora
# adresa(referenca) / vrijednost
# encapsulation
# interfejs