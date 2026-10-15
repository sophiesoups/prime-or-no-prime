import math

while True:
    number = int(input("Enter a number: "))
    prime = True

    for i in range(2, math.ceil(number)):
        if number % i == 0:
            prime = False
            break

    if prime == True:
        print("This number is prime.")
    else:
        print("This number is not prime.")

    stop = input("Do you want to try another number (y/n)? ")
    if stop != "y":
        break

