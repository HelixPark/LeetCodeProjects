
def merge(nums1,m,nums2,n):
    i,j = 0,0
    count = 0
    while i < m + n and j < n:
        if nums1[i] < nums2[j] and i < m + count:
            i += 1
        else:
            nums1.pop()
            nums1.insert(i,nums2[j])
            i += 1
            j += 1
            count += 1




nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m, n = 3, 3
merge(nums1,m,nums2,n)
