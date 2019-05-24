
def palindromenumber(x):
    x=list(str(x))

    # if x[0] == '-':
    #     return False
    for i in range(len(x)//2+1):
        if x[i] != x[len(x)-i-1]:
            return False
    return True


x = -121
palindromenumber(x)