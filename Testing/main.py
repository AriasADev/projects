def powers(a, b):
  return a**b

print("Enter a number:")
num1 = int(input())
print("Enter a second number:")
num2 = int(input())

result = powers(num1, num2)

print(f"{num1} to the power of {num2} is {result}")