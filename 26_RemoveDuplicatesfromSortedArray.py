
def removeduplicatesfromsortedarray(nums):
    for i in range(len(nums)-1,0,-1):
        tmp = nums[i]

        # if i-1 > -1 and nums[i-1] == tmp:
        #     nums.pop(i-1)
        #     i -= 1
        if nums[i-1] == tmp:
            nums.pop(i-1)
            i -= 1
    return len(nums)
        #
        # for i in range(len(nums) - 1, -1, -1):
        #     tmp = nums[i]
        #
        # if i-1 > -1 and nums[i-1] == tmp:
        #     nums.pop(i-1)
        #     i -= 1

    # return len(nums)

    # print(len(nums))



# num = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# num = [1,1,2]
num = [1,1,1]
a=removeduplicatesfromsortedarray(num)
print(num)
print(a)
print(len(num))