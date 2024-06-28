def fibonacci_generator(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_series = [0, 1]
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    
    return fib_series

# Example usage
n_terms = int(input("Enter the number of terms in the Fibonacci series: "))
fib_series = fibonacci_generator(n_terms)
print(f"Fibonacci series up to {n_terms} terms: {fib_series}")
