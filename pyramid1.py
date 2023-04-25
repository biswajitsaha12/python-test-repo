#pyramid with consecutive numbers

try:
  rows = int(input("enter number of rows: "))
  numbers=0
  if (rows < 0):
    print("Invalid input, enter a positive number")
  else:
    for i in range(rows):
      for j in range(i+1):
        numbers+=1
        print(numbers,end=' ')
      print("\r")

except ValueError:
  print("Invalid input, enter a positive number")

