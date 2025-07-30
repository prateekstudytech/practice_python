def fibonacci(n, cache):
    if n < 2:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]

# Example usage:
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i, {})}")
