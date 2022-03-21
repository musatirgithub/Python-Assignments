def isprime(num):
    prime = True
    counter = 2
    while counter < num:
        if num % counter:
            counter += 1
        else:
            prime = False
            counter += 1
            break
    return prime

print(list(filter(isprime, range(2, 100))))