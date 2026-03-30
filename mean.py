

def mean(num1, num2, num3):
    return (num1 + num2 + num3) / 3


#Kta ho run this file directly testing ko laagi

if __name__ == "__main__":
    print("=== Mean Calculator (3 Numbers) ===")
    
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        n3 = float(input("Enter third number: "))
        
        result = mean(n1, n2, n3)
        print(f"Mean = {result}")
        
    except ValueError:
        print("Invalid input! Please enter numeric values.")