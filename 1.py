import math

def sum(first_num, second_num):
    return first_num + second_num
def sub(first_num, second_num):
    return first_num - second_num
def mul(first_num, second_num):
    return first_num * second_num
def div(first_num, second_num):
    return first_num / second_num
def sin(num):
    return math.sin(num)
def cos(num):
    return math.cos(num)
def tan(num):
    return math.tan(num)

result = 0

while True:
    opertaion = str(input("input operator: "))
    try:
        if opertaion == "sin" or opertaion == "cos" or opertaion == "tan":
            num = int(input("input num: "))
        else:
            first_num = int(input("input first num: "))
            second_num = int(input("input second num: "))
    except ValueError:
        print("wrong number")
    match opertaion:
        case "+":
            result += sum(first_num, second_num)    
        case "-":
            result += sub(first_num, second_num)   
        case "*":
            result += mul(first_num, second_num) 
        case "/":
            result += div(first_num, second_num) 
        case "sin":
            result += sin(num)
        case "cos":
            result += cos(num)
        case "tan":
            result += tan(num)
        case _:
            print("wrong opertaion")
    print("solution: ", result)
    answer = str(input("do you want continue?: "))
    if answer == "y":
        continue
    else:
        break
