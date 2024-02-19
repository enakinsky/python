def delit(x):
    counter = 0
    for i in range(2,x+1):
        if(x%i==0):
            if(i%3==0):
                counter += 1
    return counter
-------------------------------
def min(x):
    y = x
    last = x
    while y > 0:
        last1 = y % 10
        if (last1%2==1):
            if last1 < last:
                last = last1
        y = y // 10
    if(last == x):
        return print("does not exist")
    else:
        return last
------------------------------
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def sum_of_divisors(num):
    def digit_product(n):
        result = 1
        for digit in str(n):
            result *= int(digit)
        return result

    def digit_sum(n):
        return sum(int(digit) for digit in str(n))

    def is_coprime(a, b):
        return gcd(a, b) == 1

    divisors_sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            if is_coprime(i, digit_sum(num)) and not is_coprime(i, digit_product(num)):
                divisors_sum += i

    return divisors_sum
