def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Input: Number of terms
num_terms = int(input("Enter the number of Fibonacci terms: "))
fibonacci(num_terms)
