def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    m = 0
    if a > 0:
        m+=1
    if b > 0:
        m+=1
    if c > 0:
        m+=1
    return m
print(main(2,-2,1))