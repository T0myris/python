# Encapsulation: intance variables and methods can be kept private.

# Abtraction: each object should only expose a high level mechanism
# for using it. It should hide internal implementation details and only
# reveal operations relvant for other objects.
# ex. HR dept setting salary using setter method

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # protected variable
        # can still be accessed outside
        self._salary = None

        # strict private variable
        # AttributeError: 'CLASS' object has no attribute '__<attribute_name>'
        # However __ is not used conventionally and _ is used.
        self.__salary = 5000

        # protected variable
        self._nums_bugs_solved = 0

    def code(self):
        self._nums_bugs_solved += 1

    # protected method
    def _calcluate_salary(self, base_value):
        if self._nums_bugs_solved < 10:
            return base_value
        elif self._nums_bugs_solved < 100:
            return base_value * 2
        return base_value

    # getter method: manual implementation
    def get_salary(self):
        return self._salary

    # getter method
    def get_nums_bugs_solved(self):
        return self._nums_bugs_solved

    # setter method
    def set_salary(self, base_value):

        value = self._calcluate_salary(base_value)

        # check value, enforce constarints
        if value < 1000:
            self._salary = 1000
        if value > 20000:
            self._salary = 20000
        self._salary = value

    # pythonic implementation of getter method
    # use @property decorator
    # name of the method is variable_name being set
    # called by print(<instance_name>.<variable_name>)
    @property
    def salary(self):
        return self._salary

    # pythonic implementation of setter method
    # use @<variable>.setter decorator
    # name of the method is variable_name being set
    # used by <instance_name>.<variable_name> = <VALUE>
    @salary.setter
    def salary(self, base_value):

        value = self._calcluate_salary(base_value)

        # check value, enforce constarints
        if value < 1000:
            self._salary = 1000
        if value > 20000:
            self._salary = 20000
        self._salary = value

    # pythonic implementation of the delete method
    # use @<variable>.deleter decorator
    # name of the method is variable_name being deleted
    # called by del <instance_name>.<variable_name>
    @salary.deleter
    def salary(self):
        del self._salary


se = SoftwareEngineer("max", 25)
print(se.age, se.name)
print(se._salary)
# print(se.__salary)

for i in range(70):
    se.code()

print(se.get_nums_bugs_solved())

se.set_salary(6000)
print(se.get_salary())

se.salary = 5000
print(se.salary)
del se.salary
print(se.salary)

'''
25 max
None
70
12000
10000
Traceback (most recent call last):
  File "/home/vibha/visual_studio/oop4.py", line 106, in <module>
    print(se.salary)
  File "/home/vibha/visual_studio/oop4.py", line 63, in salary
    return self._salary
AttributeError: 'SoftwareEngineer' object has no attribute '_salary'
'''
