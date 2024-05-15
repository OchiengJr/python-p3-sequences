def print_fibonacci(length):
    # Error handling for negative length
    if length < 0:
        print("Error: Length must be a non-negative integer.")
        return
    
    # Base cases
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    
    # Initialize the Fibonacci sequence with the first two elements
    fibonacci_sequence = [0, 1]
    
    # Generate Fibonacci sequence up to the specified length
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    # Print the Fibonacci sequence up to the specified length
    print(fibonacci_sequence[:length])

# Test the function
print_fibonacci(10)  # Example usage: prints the first 10 Fibonacci numbers
