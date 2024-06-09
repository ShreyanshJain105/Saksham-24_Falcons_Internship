'''==========================================================[fibonacci program]==============================================='''


def fibonacci(n):
  
  if n <= 1:
    return n
  a, b = 0, 1
  for i in range(2, n + 1):
    c = a + b
    a, b = b, c  # Update values for next iteration
  return c

# Example usage
number = 10
for i in range(number):
  print(fibonacci(i), end=" ")  # Print each Fibonacci number
print()  