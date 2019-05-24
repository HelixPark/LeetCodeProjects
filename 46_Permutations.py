num=[4,5,6]
def permute(nums):
    res=[]
    dfs(nums,[],res)
    return res


def dfs(nums,tmp,res):
    if not nums:   #判断nums是否为空，若nums为空返回true，执行if内语句
        res.append(tmp)
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:],tmp+[nums[i]],res)

print(permute(num))
