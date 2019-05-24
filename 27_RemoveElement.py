
def remove_element(nums,val):
    # for i in range(len(nums)-1,-1,-1):
    #     if nums[i] == val:
    #         nums.pop(i)
    return len([nums.pop(i) for i in range(len(nums)-1,-1,-1) if nums[i] == val])

    # print(len(nums))

a = [3,2,2,3]
val=2
get=remove_element(a,val)
print(a)
print(get)