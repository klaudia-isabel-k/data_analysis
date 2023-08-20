def fibonacci_loop(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)



