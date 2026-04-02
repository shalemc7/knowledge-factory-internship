#  VARIABLES & DATA TYPES 
name: str = "Shalem"          # str
age: int = 21                 # int
height: float = 5.9           # float
is_student: bool = True       # bool
phone: None = None            # NoneType
print(f"{name} | {age} | {height} | {is_student} | {phone}")

#  TYPE CONVERSION 
print(int("42") + 8)          # str → int: 50
print(str(100) + " days")     # int → str: "100 days"
print(float(25))              # int → float: 25.0
print(bool(0), bool("Hi"))    # Falsy/Truthy: False True

#  F-STRINGS 
price: float = 19.99
print(f"{name}'s item: ${price:.2f}")  # Formatting: Shalem's item: $19.99

#  ARITHMETIC OPERATORS 
a, b = 17, 5
print(a + b, a - b, a * b)    # 22 12 85
print(a / b, a // b, a % b)   # 3.4 3 2  (/, //, %)
print(a ** 2)                 # 289 (exponent)

# COMPARISON OPERATORS
x, y = 10, 15
print(x == y, x != y)         # False True
print(x > y, x <= y)          # False True
print((x + 5) >= y)           # True