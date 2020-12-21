# The most short fizzbuzz algorithm for FizzBuzz task )))

numbs = 100

fizzbuzzG = ("fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
             for x in range(1, numbs + 1))

print(*list(fizzbuzzG))
