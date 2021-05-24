lines = []
with open('numbers_list.txt','r') as f:
    lines = f.readlines()

with open('primes.txt', 'w') as f2:
    for line in lines:
        prime = line.split()[1]
        f2.write(prime + '\n' )


