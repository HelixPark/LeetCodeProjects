def inttoRoman(num):
    dic = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X',
           40:'XL', 50:'L', 90:'XC', 100:'C',
           400:'CD', 500:'D', 900:'CM', 1000:'M'}
    res = ''
    for value in sorted(dic.keys())[::-1]:
        print(value)
        tmp = num // value
        if tmp == 0:
            continue
        else:
            print(dic[value])

            res += tmp * dic[value]
            num -= tmp * value
        if num == 0:
            break
    return res


n = 1994
inttoRoman(n)