n = 0
while n == 0:
    num1 = int(input("number1: "))
    num2 = int(input("number2: "))
    oper = input("operation: ")
    if oper == "+":
        print(num1 + num2)
    elif oper == "-":
        print(num1 - num2)
    elif oper == "*":
        print(num1 * num2)
    elif oper == "/":
        print(num1 // num2)
    else:
        print("Некорректный знак")
        n = 0


