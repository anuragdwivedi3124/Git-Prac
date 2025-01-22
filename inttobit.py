# Function to convert integer to binary
def integer_to_binary(number):
    if isinstance(number, int):
        return bin(number)[2:]  # bin() converts to binary, [2:] removes the '0b' prefix
    else:
        return "Input is not an integer"

# Example usage
number = int(input("Enter an integer: "))
binary_representation = integer_to_binary(number)
print(f"Binary representation of {number} is {binary_representation}")
