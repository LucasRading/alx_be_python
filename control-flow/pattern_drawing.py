# pattern_drawing.py

# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop to handle rows
while row < size:
    # Inner for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    # Print a newline after each row
    print()
    # Move to the next row
    row += 1
