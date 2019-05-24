import math
def getPermutation(n,k):
    res=[]
    nums=[i for i in range(1,n+1)]
    while n-1 >= 0:
        # num, k =k // math.factorial(n-1), k % math.factorial(n-1)
        num =k//math.factorial(n-1)
        k=k%math.factorial(n-1)
        if k>0:   #不能整除,则只是当前的一个
            res.append(str(nums[num]))
            nums.remove(nums[num])
        else:    #能整除，则往前推一个的末尾元素
            res.append(str(nums[num-1]))
            nums.remove(nums[num-1])
        n -= 1
    return ''.join(res)   #将序列res的字符以''连接成字符串

print(getPermutation(3,3))
