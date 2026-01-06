def prime_no(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def prime_list(num):
    list_primes = []
    for i in range (2, num + 1):
        if prime_no(i):
            list_primes.append(i)
    return list_primes

num = int(input("Up to which number do you want all prime numbers: "))
print(prime_list(num))
