

def multiplyString(num1,num2):
    if num1 == '0' or num2 == '0':
        return '0'
    elif num1 == '1':
        return num2
    elif num2 == '1':
        return num1
    res = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            tmp = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            tmp += res[i + j + 1]
            res[i + j] += tmp // 10
            res[i + j + 1] = tmp % 10
            # print(res)

    res = [str(x) for x in res]
    return ''.join(res).lstrip('0')


num1="123"
num2="456"
print(multiplyString(num1,num2))