def is_balanced(testVariable, startIndex=0, currentIndex=0):
    stack = []
    for i in range(len(testVariable)):
        if testVariable[i] == '(':
            stack.append('(')
            #print(stack)
        elif testVariable[i] == ')':
            if len(stack) == 0:
                print("Parentheses not balanced at index", i)
                return False
            stack.pop()
    if len(stack) == 0:
        print("Parentheses are balanced")
        return True
    else:
        print("Parentheses not balanced")
        return False

#testVariable = ['(', '(', ')', ')', ')', '(']
num = int(input("enter no. of inputs: "))
testVariable = [] ; testlist = []
print("Enter parenthesis: ")
for i in range(num):
  testlist = input()
  testVariable.append(testlist)
print(testVariable)
is_balanced(testVariable)