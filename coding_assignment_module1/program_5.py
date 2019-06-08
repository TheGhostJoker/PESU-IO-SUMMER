#5. Answer for question - 5
str = input("Enter a string :\n")
try:
  i = float(str)
  print("The given string is numeric.")
except (ValueError, TypeError):
  print("The given string is not numeric.")
