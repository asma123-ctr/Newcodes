print("python calculator")
first_number = int(input("enter first number:"))
second_number = int(input("enter second number:"))
print("operation type")
print("+ for Addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
operator = input("please select any one of above options: ")
result = 0
if operator == "+":
    result = first_number + second_number
if operator == "-":
    result = first_number - second_number
if operator == "*":
    result = first_number * second_number
if operator == "/":
    result = first_number / second_number
else:
    print("its invalid option")
    print(f"Result:{result}")



