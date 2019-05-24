
def validparentheses(s):
    if not s:
        return True
    dic = {'(':0,')':1,'{':2,'}':3,'[':4,']':5}
    # print(dic['('])
    t = list(s[0])


    for i in s[1::]:
        if not t:   #t若为空的话，则填充进去
            t.append(i)
            continue

        tmp = t.pop()
        if dic[tmp] == dic[i]-1 and dic[i] % 2 != 0:
            continue
        else:
            t.append(tmp)
            t.append(i)
    if not t:
        return True
    else:
        return False

def isValid(s):
    while '{}' in s or '[]' in s or '()' in s:
        s = s.replace('{}','')
        s = s.replace('[]','')
        s = s.replace('()','')

    return s == ''

s = '{}({([])})'
# s = "){"
# print(validparentheses(s))
print(isValid(s))

