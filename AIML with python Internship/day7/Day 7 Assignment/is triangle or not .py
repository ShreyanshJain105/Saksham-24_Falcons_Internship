'''==========================================================[is trainglr or not  program]==============================================='''


def is_valid_triangle(a, b, c):

  if any(side <= 0 for side in (a, b, c)):
    return False

  return all(side > 0 and (a + b > c) and (a + c > b) and (b + c > a) for side in (a, b, c))

# Example usage
triangle_sides1 = (5, 12, 13)
triangle_sides2 = (3, 3, 7)  # Not a valid triangle

print(f"Triangle with sides {triangle_sides1} is valid: {is_valid_triangle(*triangle_sides1)}")
print(f"Triangle with sides {triangle_sides2} is valid: {is_valid_triangle(*triangle_sides2)}")
