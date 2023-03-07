def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    m = a % 2
    if a > 0 and m == 1:
        print("positive odd number")
    if a < 0 and m == 1:
        print("negative odd number")
    if a < 0 and m == 0:
        print("negative even number")
    if a > 0 and m == 0:
        print("positive even number")
    if a == 0:
        a = "the number is zero"
    return 
print(main(-5))