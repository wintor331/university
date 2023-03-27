def Factorial(num:int) -> int:
    sum = 1
    for i in range(num,0,-1):
        sum = sum * i
    return sum

def Combination(num:int, num2:int) -> int:
    result = Factorial(num)/(Factorial(num2)*Factorial(num-num2)) 
    return result

Factorial(3)
print(Combination(10,2))




