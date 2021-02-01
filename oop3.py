# child classes inherits, can extend or override
# all of the attributes and functions from the base class
# they can also write custom methods for themselves

# Extends is about classes. Extends represents the process of
# deriving a subclass from a base class.

# Overriding is about methods declaration and invocation.
# Overriding means to define a method in a subclass with the
# same signature of a method previously declared in its base class.

# Polymorphism allows us to define methods in the child class
# with the same name as defined in their parent class but each child class
# keeps its own methods as they are.

# base class
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} working..")

    def earn(self):
        print(f"{self.name} earns {self.salary}.")


# child class of Employee
# when overriding the base class initializer,
# super initializer should also be called
class SoftwareEngineer(Employee):

    # overriding and extending the __init__(self)
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging..")

    # overriding the base class's work() method
    # super().work() to call the base class's method
    def work(self):
        print(f"{self.name} is coding..")


# child class of Employee
# inherits instance attributes and methods (__init__(self), work(self))
# from employee class and has a custom function draw()
class Designer(Employee):

    # overriding the base class's work() method
    # super().work() to call the base class's method
    def work(self):
        print(f"{self.name} is designing..")

    # creating a new function specific to child class
    def draw(self):
        print(f"{self.name} is drawing..")


de = Designer("philip", 27, 3000)
print(de.name, de.age)
de.work()
de.earn()
de.draw()

se = SoftwareEngineer("maya", 25, 5000, "junior")
print(se.level)
se.work()

'''
philip 27
philip is designing..
philip earns 3000.
philip is drawing..
junior
maya is coding..
'''

employees = [SoftwareEngineer("Max", 30, 9000, "Senior"),
             SoftwareEngineer("Maya", 35, 12000, "Associate"),
             Designer("Mad", 30, 12000)]


def motivate_employees(employees):
    for employee in employees:
        employee.work()


motivate_employees(employees)

'''
Max is coding..
Maya is coding..
Mad is designing..
'''
