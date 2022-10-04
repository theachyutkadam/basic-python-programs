# class Employee:
#   def __init__(self, name, salary):
#     self.name = name
#     self.__salary = salary

#   # def show(self):
#   #   print("Name:", self.name, "Salary:", self.__salary)

# emp = Employee('Sunny', 125000)

# print("Employee Details:", emp.__salary)
# # emp.show()


# we can access private and protected variable suing mangling.
# class Employee:
#   def __init__(self, name, salary):
#     self.name = name
#     self.__salary = salary

#   # def show(self):
#   #   print("Name:", self.name, "Salary:", self.__salary)

# emp = Employee('Sunny', 125000)

# print("Employee Details:", emp._Employee__salary)


# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()
