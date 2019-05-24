
def longestcommonprefix1(strs):
    # 第一种，笨的方fa,考虑问题全面
    res = ""
    if len(strs) == 1:
        if strs[0] == "":
            return ""
        else:
            return strs[0]
    if not strs:
        return ""
    min_l = min([len(strs[i]) for i in range(len(strs))])
    if min_l == 0:
        return ""
    # length = len(strs)
    i, j = 0, 0

    while j < min_l:
        flag = 0
        for i in range(len(strs) - 1):
            if strs[i] == "":
                return ""
            if strs[i][j] == strs[i + 1][j]:
                flag = 1
            else:
                flag = 0
                break
        if flag:
            res += strs[i][j]
        else:
            return res
        j += 1
    return res

# **********************
#  利用python的max()和min()，
# 在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
# 所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
def longestcommonprefix2(strs):
    if not strs:
        return ""
    s1, s2 = min(strs), max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1

# ********************************************
# 利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，
# 然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀
def longestcommonprefix3(strs):
    if not strs: return ""
    ss = list(map(set, zip(*strs)))
    res = ""
    for i, x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res
# s =  ["flower","flow","flight"]
s = ["",""]
# s = ["c","c"]
# s = [""]

# print(longestcommonprefix1(s))
print(longestcommonprefix2(s))