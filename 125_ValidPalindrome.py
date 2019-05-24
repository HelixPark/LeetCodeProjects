
def ispalindrome1(s):
    # 第一种方法，传统逻辑，两头怼
    # print(chr(65))
    i, j = 0, len(s) - 1

    while i <= j:
        former = ord(s[i])
        latter = ord(s[j])
        flag1, flag2 = False, False

        if former in range(48,58) or former in range(65,91) or former in range(97,123):
            flag1 = True
        else:
            i += 1

        if latter in range(48, 58) or latter in range(65, 91) or latter in range(97, 123):
            flag2 = True
        else:
            j -= 1


        if flag1 and flag2:
            if former == latter:
                i += 1
                j -= 1
            elif former > 64 and latter > 64 and abs(former - latter) == 32:
                i += 1
                j -= 1
            else:
                return False

    return True

def ispalindrome2(s):
    # 第二种方法

    # 判断s是否只由数字和字母组成
    print(s.isalnum)

    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]


    # while i < j:
    #     if s[i] > 'A' and s[i] < 'Z':
    #         former = s[i]
    #     else:
    #         i += 1
    #
    #     if s[j] >


s = "A man, a plan, a canal: Panama"

ispalindrome2(s)