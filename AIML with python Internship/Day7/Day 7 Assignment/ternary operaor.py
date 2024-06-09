'''==========================================================[Ternary operator  program]==============================================='''


def check_number(number):
  print(1 if number > 0 else (-1 if number < 0 else 0))

# Example usage (same as previous example)
check_number(5)  # Output: 1
check_number(-3)  # Output: -1
check_number(0)  # Output: 0

