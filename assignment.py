def calculatePi(digits):
  result = 0

  for x in range(digits):
    term = 4 * ((-1) ** x) / (2 * x + 1)
    result += term
    print(f"Iteration {x + 1}: {result}")
  return result

def main():
  try:
    digits = int(input("Invalid input, please input a integer: "))
    if digits < 1:
      print("Invalid input, please input a positive integer: ")
    return

