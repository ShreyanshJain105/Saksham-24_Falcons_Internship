'''==========================================================[find out factorial program]==============================================='''


def factorial(num):
  if num < 0:
    print("Factorial is not defined for negative numbers.")
    return None  
  elif num == 0:
    return 1
  else:
    result = 1
    for i in range(1, num + 1):
      result *= i
    return result

# Example usage
number = 5
factorial_result = factorial(number)

if factorial_result is not None:  # Check for negative input error
  print(f"Factorial of {number} is: {factorial_result}")
