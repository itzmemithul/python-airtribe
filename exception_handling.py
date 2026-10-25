a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

try:
    print(a/b)
except Exception as e:
    print(f"Error: {e}")