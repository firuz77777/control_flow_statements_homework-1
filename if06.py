def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    m = 0
    if a < 0:
        m-=1
    if b < 0:
        m-=1
    if c < 0:
        m-=1
    if a > 0:
        m+=1
    if b > 0:
        m+=1
    if c > 0:
        m+=1
    if m > 0:
        print("there are a lot of positive numbers")
    if m < 0:
        print("there are a lot of negative numbers")
    return 
print(main(-2,2,2))
