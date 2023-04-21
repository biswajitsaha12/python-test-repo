try:
  def cuberoot(num, step=0.01):
    guess = 0
    guess_count = 0
    ep = 0.01
    while(abs((guess**3)-num) >= ep) and (guess<=num):
      guess += step
      #print("guess:",guess)
      guess_count+= 1
      #print("guess count:",guess_count)
      
    #print("total guesses: ",guess_count)
    if (abs((guess**3)-num) >= ep):
      return print("failed to get cube root")
    else:
      return print("approx. cuberoot is: ",guess)
      
  num = float(input("enter a positive number to find it's cuberoot: "))
  if (num < 0):
    print("Invalid input, expected a positive number")
  else:
    result = cuberoot(num)
except ValueError:
  print("Invalid input, expected a positive number")