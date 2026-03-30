def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b
def add(a, b):
    """
    Return the sum of two numbers.
    
    Parameters:
    a (int or float): First number
    b (int or float): Second number
    
    Returns:
    int or float: Sum of a and b
    """
    return a + b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4/5): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(a, b))
elif choice == '2':
    print("Result:", subtract(a, b))
elif choice == '3':
    print("Result:", multiply(a, b))
elif choice == '4':
    print("Result:", divide(a, b))
else:
    print("Invalid choice")