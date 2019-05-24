
# 典型的用动态规划求解

def maximumsubarray(nums):
    # if not nums:
    #     return 0
    if len(nums) == 0:
        return 0
    dp=[0]*len(nums)
    res,dp[0]=nums[0],nums[0]
    for i in range(1,len(nums)):
        dp[i]=max(dp[i-1]+nums[i],nums[i])
        res=max(dp[i],res)
    return res

    # return [max(res,max(dp[i-1]+nums[i],nums[i])) for i in range(1,len(nums))]

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maximumsubarray(nums))