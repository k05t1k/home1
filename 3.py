def IsEvenNum(num):
    if num % 2 == 0:
       return True
    else:
       return False
    
number = int(input('input number: '))
if (IsEvenNum(number)):
   print("is an even number")
else:
   print("isn't an even number")