
def wildcardmatching(s,p):
    m,n=len(s),len(p)
    # 创建动态规划矩阵
    dp=[[bool(0) for i in range(n+1)] for j in range(m+1)]
    # print(dp)
    dp[0][0]=bool(1)

    # 初始化填充，如果s为空的话，只有*的模式才能匹配
    for i in range(n):
        if dp[0][i] and p[i] == '*':
            dp[0][i+1]=bool(1)
    # 动态规划
    for i in range(m):
        for j in range(n):
            if p[j] == '*':
                dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
            elif p[j] == '?' or s[i] == p[j]:
                dp[i+1][j+1] = dp[i][j]
    return dp[m][n]


wildcardmatching("adceb","*a*b")
