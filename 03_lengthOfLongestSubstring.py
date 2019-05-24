# s = input("input string:")

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# tmp作为字典，存储无重复的字符和位置下标
# j为游标，i为左标志，随着j往右走，若s[j]在tmp中未出现，则把s[j]放在tmp中，反之，
# 则比较前后出现的位置，选择大(也就是后者),更新tmp位置，i的位置也随之更新

def lengthOfLonfestSubstring(s):
    temp = {}  # 字典存放s中的字母的最新位置，无重复
    i, ans = -1, 0  # i为起始位置，ans表示最长的无重复子串，表示最初重复的位置
    for j in range(len(s)):
        if s[j] in temp:
            i = max(temp[s[j]], i)
        ans = max(ans, j - i)   #若i j之间未重复，则最长子串为j-i，反之还是ans
        temp[s[j]] = j
    return ans

# 测试样例
test_s=["abcabcbb","bbbbb","pwwkew"]

# for ss in test_s:
#     print(lengthOfLonfestSubstring(ss))

# 列表解析的两种方式，因为是列表解析，所以方括号必须带
L=[lengthOfLonfestSubstring(ss) for ss in test_s]
print(L)
print([lengthOfLonfestSubstring(ss) for ss in test_s])

def createGirlFriend(s):
    print("new a gf")
    tmp={}   #空字典
    left=-1
    ans=0
    for j in range(len(s)):
        if s[j] in tmp:
            left=max(tmp[s[j]],left)
        ans=max(ans,j-left)   #选最大的长度
        tmp[s[j]]=j
    return ans

print([createGirlFriend(ss) for ss in test_s])
l=9
print(l/2)
print(l//2)