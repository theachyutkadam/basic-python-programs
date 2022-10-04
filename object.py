# class Student:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("The name of student is:- " + self.name)

#   def log_line(self):
#     print("foo00000000000000000000000")

# student1 = Student("achyut", 33)
# print(student1.show_details())
# student1.log_line(12)



# from turtle import setx
# from unicodedata import name

class Student:
  def __init__(self, name, gender, profession) -> None:
    self.name = name
    self.gender = gender
    self.profession = profession

  def show(self):
    print('Name:-', self.name, 'Gender:-', self.gender, 'Work:- ', self.profession)

  def work(self):
    print(self.name, "Working as a", self.profession)

kadam = Student("achyut", 26, "software developer")
kadam.show()
kadam.work()
