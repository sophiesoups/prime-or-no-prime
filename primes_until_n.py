import math

while True:
    primes = []
    number = int(input("Enter a number: "))

    for i in range(2, number + 1):
        prime = True
        for j in range(2, math.ceil(i / 2)):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            primes.append(i)

    results = [prime for prime in primes]
    print(results)


    stop = input("Do you want to try another number (y/n)? ")
    if stop != "y":
        break

