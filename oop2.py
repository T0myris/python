
# position, name, age, level, salary
se1 = ["SE", "Maya", "20", "Senior", "7000"]
se2 = ["SE", "Max", "30", "Junior", "2000"]
d1 = ["Designer", "Art"]


# global method
def gcode(se):
    print(f"{se[1]} is writing code...")


# gcode(se2)
# gcode(d1)


# class
class SoftwareEngineer:

    # class attribute: is same for every instance
    alias = "Keyboard Magician"

    # instance attributes defined in __init__(self)
    def __init__(self, name, age, level, salary):

        # instance attributes: the value tied to one instance
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance methods
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing in {language}")

    def information(self):
        information = f"name:{self.name},age:{self.age},level:{self.level}"
        return information

    # dunder method, already implemented for each class by default
    # __str__(self) always need to return something in custom implementation
    # default prints the memory location of the object,
    # called by print(instance)
    def __str__(self):
        information = f"name:{self.name},age:{self.age},level:{self.level}"
        return information

    # default compares the memory address,
    # called by instance1 == instance2
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # what happens if we don't pass self and call from an instance: crash
    # TypeError: entry_salary() takes 1 positional argument but 2 were given
    # however, this function can be used for the class: CLASS.method(args)
    def entry_salary1(age):
        if age < 25:
            return 5000
        if age < 30:
            return 6000

    # by using @staticmethod decorator, it won't crash if called by an instance
    # static method not tied to a particular instance, as
    # self.<attribute> cannot be accessed
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 6000


# instance
se2 = SoftwareEngineer("Maya", "20", "Senior", "7000")
se3 = SoftwareEngineer("Maya", "20", "Junior", "7000")
se1 = SoftwareEngineer("Max", "10", "Junior", "2000")
print(se1.name, se1.age)
print(se1.alias == se2.alias, se1.alias == SoftwareEngineer.alias)
se1.code()
# se2.code()
# se1.code_in_language("python")
se2.code_in_language("scala")
# print(se1.information())
# print(se2.information())

print(se1)
print(se3 == se2)

# se1.entry_salary1(24) # crashes
print(SoftwareEngineer.entry_salary1(24))

print(se1.entry_salary(24))
print(SoftwareEngineer.entry_salary(24))

'''
Max 10
True True
Max is writing code...
Maya is writing in scala
name:Max,age:10,level:Junior
True
5000
5000
5000
'''
