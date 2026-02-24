"""number = 5
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print (factorial)

def factor(num):
    if num == 1: return 1
    return num * factor(num-1)
print(factor(5))"""


number = 10
sequence = [1,1]
for i in range(1,number):
    sequence.append(sequence[i] + sequence[i-1])
    """print (sequence)"""
r_s = [1,1]
def fib(n):
    if n == 1: return 1
    elif n == 2: return 1
    else: r_s.append(r_s[fib(n)] + r_s[n-1])
print (fib(10))
