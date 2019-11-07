import numpy as np
import time


def sieve_of_eratosthenes(n):
    is_prime = np.ones(n, dtype=bool)
    is_prime[:2] = False  # 0 and 1 are not primes

    for i in range(2, int(np.sqrt(n))):
        if not is_prime[i]:
            continue
        is_prime[i*i::i] = False

    return np.nonzero(is_prime)[0]


num = int(input('Enter a number: '))
start_time = time.time()
sieve_of_eratosthenes(num)
print("--- %s seconds ---" % (time.time() - start_time))
