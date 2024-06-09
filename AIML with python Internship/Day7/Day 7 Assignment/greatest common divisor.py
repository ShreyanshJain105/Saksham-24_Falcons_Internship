'''==========================================================[GCD program]==============================================='''


def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

# Example usage
num1 = 12
num2 = 18
gcd_result = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {gcd_result}")
