def func(num):
    if num > 0 and isinstance(num, int):
        sum = 0
        while num > 0:
            v68 = num % 10
            sum += v68
            num = num // 10
        return sum

try:
    number = int(input("input number: "))
    print(func(number))
except ValueError:
    print("error")
