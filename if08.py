def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    q = a // 10

    if q < 10 and a % 2 == 0:
        print("two-digit even number")
    if q < 10 and a % 2 == 1:
        print("two-digit odd number")
    if q >= 10 and a % 2 == 1:
        print("three-digit odd number")
    if q >= 10 and a % 2 == 0:
        print("three-digit even number")
    return 
print(main(96))