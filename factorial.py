# Function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Main program
def main():
    # Get user input
    try:
        num = int(input("Enter a number to find it's factorial: "))
        
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            # Calculate factorial
            result = factorial(num)
            print(f"The factorial of {num} is {result}")
    except ValueError:
        print("Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    main()
