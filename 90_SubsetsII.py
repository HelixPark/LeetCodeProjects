
def subsets_II(nums):
    # print(nums)
    nums.sort()
    # print(nums)
    builder=[[]]
    for i in  nums:
        tmp=[j for j in builder]
        for t in tmp:
            builder.append([i]+t)
    builder.sort()
    cur,res=builder[0],[builder[0]]
    for i in builder:
        if i != cur:
            res.append(i)
            cur = i
    return res

a=[1,2,2]
s=subsets_II(a)
print(s)