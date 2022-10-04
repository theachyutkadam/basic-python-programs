from unicodedata import name


class Student:
  school_name = "Anisha Global School"

  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def check_info(self):
    print("####################")
    employee_name = "achyut kadam"
    print("####################")

  def print_name(self):
    self.check_info()
    print("####################")
    # print(employee_name)

student1 = Student("achyut", 26)
# student1.check_info()
student1.print_name()

# print("Emp Name:-" student1.print_name)

# print("Student:- ", student1.name, student1.age)
# print("School:- ", Student.school_name)

# student1.name = "Ravi"
# student1.age = 25
# print("Student:- ", student1.name, student1.age)

# Student.school_name = "Microsoft School"
# print("School:- ", Student.school_name)


