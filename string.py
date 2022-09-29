txt = "this is the testing program, and learning the python."

multiline ="""
Hello
Mr Kadam
How are you?"""

print("kadam" not in txt)

print("testing" in txt)
if "testing" in txt:
  print("Yes, testing is present in txt")

print(multiline)

b = "Hello, World!"
print(b[1:8])
print(b[:8])
print(b[2:])
first_name = "Achyut"
last_name = "Kadam"
print(first_name + " " + last_name)

# list = array
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
test = ["apple", 12, 4.33, 3333]
print(test)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# tuple - allow duplicate value
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
