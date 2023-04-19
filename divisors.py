#Find divisors of a number
try:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Negative number detected! Enter a positive integer")
    else:
        divisors = [i for i in range(num, 0, -1) if num % i == 0]
        print("List of divisors: ", divisors) 
except ValueError:
    print("Invalid input! Enter a positive integer")
