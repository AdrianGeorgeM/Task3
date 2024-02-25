def fibonacci(n):
    """
    Calculate the n-th Fibonacci number using recursion.

    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1. This function
    uses recursion to calculate the n-th number in the sequence.

    Args:
        n (int): The position in the Fibonacci sequence to calculate.

    Returns:
        int: The n-th Fibonacci number.
    """

    # Base case: the first and second numbers in the sequence are 1
    if n <= 1:
        return n

    # Recursive case: sum of the two preceding numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage of the function
if __name__ == "__main__":
    n = 10
    print(f"The {n}-th Fibonacci number is: {fibonacci(n)}")
