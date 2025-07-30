def fibonacci(n: int) -> list:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")
