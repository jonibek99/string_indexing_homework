def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if n in s:
        return str(s).index(n)
    return False
a=str(input('please enter the argument of S\n'))
b=str(input('please enter the argument of N\n'))
print(main(a,b))