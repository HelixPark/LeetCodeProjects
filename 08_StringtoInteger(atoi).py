
def stringtointeger_01(str):
    # print()
    str = list(str.strip())
    if len(str) == 0:
        print("NULL")
        return 0
    # if not  str:
    #     return 0

    # 用ascii比较
    head=str.pop(0)
    if head != '+' and head != '-' and (head > '9' or head <'0'):
        return 0

    for i in str:
        if i > '9' or i < '0':
            break
        head += i
    if head == '-' or head == '+':
        return 0
    return -2**31 if int(head)<-2**31 else int(head) if int(head)<2**31-1 else 2**31-1

def stringtointeger_02(str):
    # print()
    str = list(str.strip())
    if len(str) == 0:
        print("NULL")
        return 0
    # if not  str:
    #     return 0

    # 用list num查找
    nums='0123456789'
    head=str.pop(0)
    if head != '+' and head != '-' and head not in nums:
        return 0

    for i in str:
        if i not in nums:
            break
        head += i

    if head == '-' or head == '+':
        return 0

    return -2**31 if int(head)<-2**31   else int(head) if int(head)<2**31-1 else 2**31-1
import re
def stringtointeger_03(str):
    # 用正则表达式匹配模块
    if not str or str == '' or str.strip() == '' :
        return 0
    str=str.strip()
    pattern = re.compile(u"^[-,+]?\d+")
    ret=pattern.findall(str)
    if len(ret)==0:
        return 0
    if len(ret)==1:
        if int(ret[0]) < -2**31:
            return  -2**31
        if int(ret[0] > 2**31-1):
            return 2**31-1
        return int(ret[0])


print(stringtointeger_03("-91283472332"))