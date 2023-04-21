try:
  def cuberoot(num, step=0):
    guess = 0
    #print(num)
    while(abs((guess**3)-num) > 0.0001):
      diff = abs((guess**3)-num)
      #print("diff: ", diff)
      if (diff < num):
        step = step + 1
        #print("+ve step: ",step)
        guess += step
        #print("+ve guess :",guess)
      else:
        step = step - 1
        #print("-ve step: ",step)
        guess -= step
        #print("-ve guess :",guess)
    #print("final diff: ",abs((guess**3)-num))    
    return guess

  num = int(input("enter a positive number: "))
  if (num < 0):
    print("Invalid input, expected a positive number")
  else:
    result = cuberoot(num)
    print("cuberoot is: ", result)
except ValueError:
  print("Invalid input, expected a positive number")