__author__ = 'onotole'

def fibanocci(number):
    n0=1
    n1=1
    for i in range(number):
        n0,n1= n1, n0+n1
    return n0

print (fibanocci(10))