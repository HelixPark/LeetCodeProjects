
def lengthoflastword(s):
    ss = s
    p1 = s.index(' ',0,len(s)-1)
    print(p1)
    p2 = s.find(' ')
    print(p2)



    #第一种方法
    print(len(s.strip().split(' ').pop()))
    len(s.strip().split(' ').pop())

    # 第二种方法
    i = len(ss) - 1
    count = 0
    while i >= 0 and ss[i] == ' ':
        i -= 1
    while i >= 0 and ss[i] != ' ':
        i -= 1
        count += 1
    print(count)



s = '   Hello world, i want you '
lengthoflastword(s)