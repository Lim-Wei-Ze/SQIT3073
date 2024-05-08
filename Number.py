# Get user input for integer and floating-point numbers
m = float(input("Enter a number (m): "))
n = float(input("Enter another number (n): "))
p = int(input("Enter an integer (p): "))

# Perform arithmetic operations
sum_mn = m + n
difference_mp = m - p
product_np = n * p
quotient_mn = m / n
modulus_mn = m % n
exponentiation_mn = m ** n

# Print the results
print("m + n =", sum_mn)
print("m - p =", difference_mp)
print("n * p =", product_np)
print("m / n =", quotient_mn)
print("m % n =", modulus_mn)
print("m ** n =", exponentiation_mn)

# Use built-in functions for numerical operations
absolute_p = abs(p)
rounded_n = round(n)
max_value = max(m, n, p)
min_value = min(m, n, p)

print("Absolute value of p:", absolute_p)
print("Rounded value of n:", rounded_n)
print("Max value:", max_value)
print("Min value:", min_value)

# Import the math module for more advanced math operations
import math

square_root_m = math.sqrt(m)
logarithm_base_10_m = math.log10(m)
factorial_p = math.factorial(abs(p))

print("Square root of m:", square_root_m)
print("Logarithm base 10 of m:", logarithm_base_10_m)
print(f"Factorial of |p| ({abs(p)}):", factorial_p)

# Modified for Activity (2 May 24) by LIM WEI ZE (292005)
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my
