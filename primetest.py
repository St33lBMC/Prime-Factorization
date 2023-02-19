#small script that finds factors of a prime number
#uses the sieve of Erectionclese or something like that idk

import math


pq = 120521
print("factors of " + str(pq) + ":")
for i in range(2, int(math.sqrt(pq))):
    if ((pq % i) == 0):
        print(i)
        print(pq / i)