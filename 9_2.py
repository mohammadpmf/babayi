primes = []
n = int(input("Enter n: "))
for i in range(1, n+1):
    primes.append(i)
primes.remove(1)
for number in primes:
    if number*number in primes:
        for j in range(2, primes[-1]//2+1):
            if j*number in primes:
                primes.remove(number*j)
print(f"There are {len(primes)} prime numbers between 1 and {n}\n{primes}")
input("Press Enter to end program")
