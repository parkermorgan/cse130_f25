def fib(n):
    if n <= 1:
        return n
    else:
        return fib( n - 1) + fib( n - 2)
    
test_cases = [0, 1, 2, 3, 4, 5]

for case in test_cases:
    print(fib(case))