#H.W 3 (Calculator using Function)
def calFun(a,op,b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        print("Wrong operator")
x = float(input("Enter the 1st value: "))
z = input("Use any Operator '+','-','*','/'\n")
y = float(input("Enter the 2nd value: "))
print("The ans is: ",calFun(x,z,y))
