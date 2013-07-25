__author__ = 'onotole'
import itertools
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

for i in itertools.count(2):
    if isprime(i):
        print (i)
        print("Do you want more? y/n:")
        answer = input()
        if answer != "y":
            break
