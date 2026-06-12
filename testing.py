from datetime import datetime

# Function
def greet(name):
    print(f"\nHello, {name}! Welcome to Python.\n")

# User Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

greet(name)

# Variables
print("===== USER details=====")
print("Name:", name)
print("Age:", age)

# Addition
print("\n===== ADDITION =====")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2
print("Sum =", total)

# Even/Odd
print("\n===== EVEN OR ODD =====")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

# Loop
print("\n===== COUNTING 1 TO 10 =====")
for i in range(1, 11):
    print(i)

# Multiplication Table
print("\n===== MULTIPLICATION TABLE =====")
table_num = int(input("Enter a number for table: "))

for i in range(1, 11):
    print(f"{table_num} x {i} = {table_num * i}")

# List Example
print("\n===== SERVER LIST =====")
servers = ["web01", "web02", "db01"]

for server in servers:
    print(f"Checking server: {server}")

# Current Date and Time
print("\n===== DATE & TIME =====")
now = datetime.now()
print("Current Date & Time:", now)

# DevOps Style Status Check
print("\n===== SERVER STATUS =====")
for server in servers:
    print(f"Server {server} is UP")

print("\nProgram Completed Successfully!")