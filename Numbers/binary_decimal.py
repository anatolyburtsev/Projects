__author__ = 'onotole'


def bin_to_dec(number):
    sum=0
    for i in range(len(str(number))):
        if str(number)[i] == '1':
            sum += 2**(len(str(number))-i-1)
    return sum


def dec_to_bin(number):
    answer = ''
    while number > 0:
        answer += str(number % 2)
        number //= 2
    return answer[::-1]

print(bin_to_dec(dec_to_bin(555)))
