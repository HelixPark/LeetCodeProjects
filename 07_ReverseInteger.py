
def reverseinteger(x):
    if x == 0:
        return 0
    x_str=str(x)
    res=''
    if x_str[0] == '-':
        res += '-'
    res += x_str[len(x_str)-1::-1].lstrip('0').rstrip('-')
    res=int(res)
    if -2**31<res<2**32-1:
        return res
    return 0
print(reverseinteger(-12340))