

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))

try:
    ans = num1/num2
    print('Answer = ',ans)
except:
    print("Cannot divide number by 0. Use another number")
