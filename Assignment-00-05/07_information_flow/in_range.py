def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if low <= n <= high:
        return True
    return False

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    if in_range(n, low, high):
        print("The number is in range.")
    else:
        print("The number is out of range.")

if __name__ == '__main__':
    main()
