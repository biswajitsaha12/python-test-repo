try:
  def cuberoot(n):
    start = 0
    end = n
    e = 0.001
    
    while (True) :
      mid = (start + end) / 2
      diff = abs((mid**3 - n))
      n_steps = n_steps + 1
      
      if (diff <= e):
        return mid       
      elif ((mid**3) > n) :
        end = mid
      else:
        start = mid
               
  n = float(input("enter number: "))
  if (n<0):
    print("Invalid input, expected a positive number")
  else:
    result = cuberoot(n)
    print("Cube root is", round(result,3))

except ValueError:
  print("Invalid input, expected a positive number")
