def type_prime_numbers(number):  

    primes = []
    for prime in range(2, int(number) + 1):
        isPrime = True
        for num in range(2, int(prime ** 0.5) + 1):
            if prime % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(prime)
    
    return (primes)


number = input("Please enter a number:")
primes = type_prime_numbers(number)
for p in range(len(primes)):
    print(primes[p], end=" ")