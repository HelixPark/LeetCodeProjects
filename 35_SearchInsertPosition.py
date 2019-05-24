
def searchinsertposition(nums,target):

    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)
    # return nums.index(target) if target in nums else return nums.append(target), nums.sort() , nums.index(target)
num = [0, 0, 1, 1, 1, 3, 3, 4]
tar=2
print(searchinsertposition(num,tar))