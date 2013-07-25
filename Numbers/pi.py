__author__ = 'onotole'
import itertools

def pi(number):
    # pi/4=1-1/3+1/5-1/7+1/9-...
    sum=0
    for next_term in itertools.count(start=0, step=1):
        sum += (-1)**next_term*(1/(next_term*2+1))
        if next_term*2+1>10**number:
            break
    return 4*sum

print(pi(5))

