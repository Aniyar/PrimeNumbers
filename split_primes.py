with open('primes.txt','r') as f:
    lines = f.readlines()

list1, list2 = [], []
for i in range(len(lines)):
    if i % 2 == 0:
        list1.append(lines[i].strip())
    else:
        list2.append(lines[i].strip())

with open('primes1.txt','w') as f1:
    for i in list1:
        f1.write(i + '\n')
    
with open('primes2.txt','w') as f2:
    for i in list2:
        f2.write(i + '\n')
