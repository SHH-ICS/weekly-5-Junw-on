def calculatePi(digits):
  try:
    result = 0
    if int(digits) < 0:
      result = "Invalid input"
      return result
    for x in range(int(digits)):
      x = x - 1
      result = result + ((-1) ** x) / (2 * x + 1)
  except:
    result = "Invalid input"
  return result

numberofdigits = input()
print(4 * calculatePi(numberofdigits))
