__author__ = 'onotole'

def not_prime(number):
    for i in range(2, number//2+1):
        if number%i==0:
            return i
    return False

def factorization(number):
    n=number
    multipliers = []
    divisor=not_prime(n)
    while divisor:
        n//=divisor
        multipliers.append(divisor)
        divisor=not_prime(n)
    multipliers.append(n)
    return multipliers

print ("Please input number for factorization:")
x = input()
try:
    print (factorization(int(x)))
except ValueError:
    print("It is not number!")