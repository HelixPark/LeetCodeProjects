
def nextpermutation(nums):
    print(nums)
    # 从末尾往前找到一个升序排列的最后一个元素位置i，
    # 然后再从末尾往i处找到第一个大于i-1 位置处的元素，进行交换
    # 最后前后转置i 到末尾的所有元素
    # 但这时的数组还不是最小的，因为最小的排序是升序排列，所以对于[i...nums.length - 1]，需要将其变为升序，因为[i...nums.length - 1]
    # 原为降序排列，所以直接两两倒转即可变为升序

    head = 0
    length = len(nums)
    for i in range(length - 1,0,-1):
        if nums[i - 1] < nums[i]:
            # flag = True
            head = i
            former, latter = i - 1, length - 1
            while latter >= former:
                if nums[latter] > nums[former]:
                    tmp = nums[former]
                    nums[former] = nums[latter]
                    nums[latter] = tmp
                    break
                else:
                    latter -= 1
            break

    # print(i)
    former, latter = head, length - 1
    while latter > former:
        tmp = nums[latter]
        nums[latter] = nums[former]
        nums[former] = tmp
        latter, former = latter - 1, former + 1
    # [print(nums[k]) for k in range(length)]

# nums = [1,2,5,7,4,3,1]

# nums = [7,8,6,1,2,5,4,3]
# nums = [7,8,6,1,3,2,4,5]
nums = [3,2,1]
nextpermutation(nums)