# i = 1
# while i < 6:
#   print(i)
#   if i ==3:
#     break
#   i += 1

# for x in range(6):
#   for i in range(x+1):
#     print(i, end=" ")
#   print("\r")

# print("--"*5)
# for x in range(6):
#   print(f"{x} "*x)

# n=1;i=5
# while(i>=n):
#   print(" " * (n-i) +f"{i}" * i)
#   i-=1


def piramid(lines):
  n=lines;i=0
  while(i<=n):
    # print(" " * (n - i) +"* " * i)
    print(" " * (n-i) +"* " * i)
    i+=1

  n=1;i=lines
  while(i>=n):
    print(" " * (n-i) +f"{i}" * i)
    i-=1

piramid(5)
