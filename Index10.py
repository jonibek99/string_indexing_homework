def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=0
    b=[]
    for i in (s):
        a+=int(i)
        b.append(a)
    return b[-1]
l=input()
print(main(l))