# print("Enter Your Name:- ")
# name =
# print("Enter Your Birth Year:- ")
# birth_year =

from multiprocessing.sharedctypes import Value


name = input("Enter your name: ") # String Input.
age = int(input("Enter your age: ")) # Integer Input.
if age > 18:
  print("Congratulation, You are Eligibilate to Vote")
else:
  print(f"Try after {18-age} year")
