def is_prime(number):
    """Return True if *number* is prime."""
    if number <= 1:  #All negative numbers should return False
        return False
    #if number in (0, 1): #Since excluded, both should return False
        #return False
    for element in range(2, number): #Modulo 0 raises an exception. Modulo 1 always returns True. Exclude them
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
