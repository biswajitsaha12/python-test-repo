num = int(input("Enter a number: "))
divisors = [i for i in range(num, 0, -1) if num % i == 0]
print("List of divisors: ", divisors)