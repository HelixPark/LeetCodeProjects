
def foursum(nums,target):
    # 思路：借用三数之和的思路，外部两重循环，再添加双指针
    # 先数组排序，在定义一个i指针，再定义两个指针former、latter
    # 首先i循环，然后former、latter在i之后循环
    # 判断是否有符合条案件的三元组，若有则更新former、latter位置
    # 在former《latter的范围内若有重复的则直接跳过
    nums.sort()
    print(nums)
    res = []
    l = len(nums)

    for i in range(l):
        for j in range(i+1,l,1):
            former, latter = j+1, l-1
            while former < latter:
                tmp = nums[j] + nums[former] + nums[latter]
                if tmp == target - nums[i]:
                    if [nums[i],nums[j],nums[former],nums[latter]] not in res:
                        res.append([nums[i], nums[j], nums[former], nums[latter]])
                    former += 1
                    latter -= 1
                    while former < latter and nums[former] == nums[former-1]:
                        former += 1
                    while former < latter and nums[latter] == nums[latter+1]:
                        latter -= 1
                elif tmp > target - nums[i]:
                    latter -= 1
                else:
                    former += 1
    return res


# s = [1, 0, -1, 0, -2, 2]
# s = [0,0,0,0]
# s = [-3,-2,-1,0,0,1,2,3]
# target = 0
s = [-1,0,-5,-2,-2,-4,0,1,-2]

target = -9
print(foursum(s,target))
