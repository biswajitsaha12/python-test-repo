#pyramid triangle

try:
  rows = int(input("enter number of rows: "))
  if (rows < 0):
    print("Invalid input, enter a positive number")
  else:
    num = 1
    for i in range(1,rows+1):
      print(" " * (rows - i), end ='')
      for j in range(1, i+1):
          print("{:02d}".format(num), end=" ")
          num += 1
      print("\r")

except ValueError:
  print("Invalid input, enter a positive number")

