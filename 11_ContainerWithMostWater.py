
# 暴力法
def maxArea1(height):
    # 暴力法
    res = 0
    for i in range(len(height)):
        for j in range(i+1,len(height),1):
            area = min(height[i],height[j]) * (j - i)
            if area > res:
                res = area
    return res

def maxArea2(height):
    # 双指针法
    former, latter = 0, len(height)-1
    res = 0
    while former < latter:
        res = max(res , min(height[former],height[latter]) * (latter - former))
        if height[former] < height[latter]:
            former += 1
        else:
            latter -= 1
    return res

h = [1,8,6,2,5,4,8,3,7]
print(maxArea2(h))