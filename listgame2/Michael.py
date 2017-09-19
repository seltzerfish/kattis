import time
import random
from math import gcd


def pollardIsPrime(n):
    if n == 1:
        return True
    if n != 2 and n % 2 == 0:
        return False
    if isPrime(n):
        return True  # define it somehow, e.g. return False, then it infinite loops on primes
    while True:
        c = random.randint(2, n - 1)

        def f(x): return x**2 + c
        x = y = 2
        d = 1
        while d == 1:
            x = f(x) % n
            y = f(f(y)) % n
            d = gcd((x - y) % n, n)
        if d != n:
            return False


def isPrime(num):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabinMiller().

    if (num < 2):
        return False  # 0, 1, and negative numbers are not prime

    # About 1/3 of the time we can quickly determine if num is not prime
    # by dividing by the first few dozen prime numbers. This is quicker
    # than rabinMiller(), but unlike rabinMiller() is not guaranteed to
    # prove that a number is prime.
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    if num in lowPrimes:
        return True

    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if (num % prime == 0):
            return False

    # If all else fails, call rabinMiller() to determine if num is a prime.
    # return rabinMiller(num)
    return True


def rabinMiller(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5):  # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:  # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def remove_duplicates(l):
    i = 0
    for j in range(1, len(l)):
        if l[i] == l[j]:
            k = l[i] * l[len(l) - 1]
            del l[j]
            del l[i]
            l.append(k)
            break
        i += 1
    l.sort()
    return l


def backtrack(factors_list, number):
    cur_highest = list(factors_list)
    number_backup = number
    list_copy = list(factors_list)
    for x in range(1, len(factors_list) + 1):
        for y in range(1, x):
            list_copy.pop()
        skip = list_copy.pop() + 1
        for z in list_copy:
            number //= z
        while skip <= number**0.5:
            checkint = number / skip
            if checkint == int(checkint):
                list_copy.append(skip)
                number //= skip
            skip += 1
        if number != 1:
            list_copy.append(number)
        list_copy = set(list_copy)
        if len(list_copy) > len(cur_highest):
            return list_copy
        list_copy = list(factors_list)
        number = number_backup
    return cur_highest


def pollard2():
    if n % 2 == 0:
        return 2
        return 2
    while True:
        c = random.randint(2, n - 1)

        def f(x): return x**2 + c
        x = y = 2
        d = 1
        while d == 1:
            x = f(x) % n
            y = f(f(y)) % n
            d = gcd(abs(x - y) % n, n)
        if d != n:
            return d


def solve(inp):
    if inp < 2:
        return 0
    factors_list = []
    if pollardIsPrime(inp):
        return 1
    i = int((inp**.5) - 1)
    number = inp

    while i != 0:
        if inp % i == 0:
            factors_list.append(i)
            inp //= i
        i -= 1
    if len(factors_list) == len(set(factors_list)) == 2 and all(pollardIsPrime(z) for z in factors_list):
        return len(factors_list)
    if inp != 1:
        factors_list.append(inp)
    factors_list.sort()
    if len(factors_list) != len(set(factors_list)):
        factors_list = set(factors_list)
    factors_list = backtrack(factors_list, number)
    return len(factors_list)


if __name__ == '__main__':

    inp = int(input())
    start_time = time.time()
    print(solve(inp))
    finish_time = time.time()
    print(finish_time - start_time)
    #print(time.time() - start_time)
