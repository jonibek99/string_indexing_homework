def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=''
    b=[]
    for i in str(s):
        if i in '1234567890':
            a+=i
            b.append(a)
    return b[-1]
l=str(input())
p=(main(l))
print(int(p))
        