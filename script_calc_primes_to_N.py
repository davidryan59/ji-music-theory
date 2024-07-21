import csv

# Script to calculate all the primes up to MAX_N
MAX_N = 100000

primes = []
counter = 1
add = 4
while counter + add <= MAX_N:
    counter += add  # 5, 7, 11, 13...
    add = 6 - add  # 4, 2, 4, 2, 4, 2...

    is_composite = False
    for prime in primes:
        if counter % prime == 0:
            # print(f"reject {counter=}, {prime=}")
            is_composite = True
            break

        if prime * prime > counter:
            break  # this line gives massive speed-up, by eliminating redundant checks

    if not is_composite:
        # print(f"{counter=} is prime")
        primes.append(counter)

primes = [2, 3, *primes]  # don't need to check for 2 or 3 earlier, since neither 2 nor 3 divide into 5, 7, 11, 13...
# print(primes)

# output the primes to a CSV file
filename = f"primes_to_{MAX_N}.csv" 
with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["p"])
    for prime in primes:
        csvwriter.writerow([prime])

print(f"from 1 to {MAX_N} there are {len(primes)} primes, these have been written to {filename}")
