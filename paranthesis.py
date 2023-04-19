import re

def balanced(testV, index=0, count=[0,0,0]):
  if index == len(testV):
    if count[0]==0 and count[1]==0 and count[2]==0:
      print("parenthesis are balanced")
      return True
    else:
      print("parenthesis are not balanced at iteration: ", index)
      return False
  elif re.search(r"\w",str(testV[index])):
    return balanced(testV,index+1,count)
  elif testV[index] == '(':
    count[0]+=1
    return balanced(testV,index+1,count)
  elif testV[index] == '[':
    count[1]+=1
    return balanced(testV,index+1,count)
  elif testV[index] == '{':
    count[2]+=1  
    return balanced(testV,index+1,count)
  elif testV[index] == ')':
    if count[0]>0:
      count[0]-=1
      return balanced(testV,index+1,count)
    else:
      print("parenthesis order incorrect!, at index: ",index)
      
  elif testV[index] == ']':
    if count[1]>0:
      count[1]-=1
      return balanced(testV,index+1,count)
    else:
      print("parenthesis order incorrect!, at index: ",index)
      
  elif testV[index] == '}':
    if count[2]>0:
      count[2]-=1
      return balanced(testV,index+1,count)
    else:
      print("parenthesis order incorrect!, at index: ",index)
      
  else:
    print("invalid input, expected parenthesis or alphanumeric characters")
    return False


testV=list(input("input string: "))
balanced(testV)