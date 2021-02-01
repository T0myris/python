
# position, name, age, level, salary
se2 = ["SE", "Maya", "20", "Senior", "7000"]
se2 = ["SE", "Max", "10", "Junior", "2000"]


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


# instance
se2 = SoftwareEngineer("Maya", "20", "Senior", "7000")
se1 = SoftwareEngineer("Max", "10", "Junior", "2000")
print(se1.name, se1.age)
print(SoftwareEngineer.alias)
print(se1.alias == se2.alias)

'''
Max 10
Keyboard Magician
True
'''
