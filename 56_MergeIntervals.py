
# def merge(intervals:list[list[int]]) -> list[list[int]]:
def merge(intervals):
    if not intervals:
        return intervals
    # 先正序排列，再从右往左依次比较(倒序比较)
    intervals = sorted(intervals, key=lambda x: x[1])
    # sorted(intervals,key=lambda x:x[0])
    l1 = len(intervals)
    res = [intervals[l1-1]]

    for i in range(l1-2,-1,-1):
        if res[0][0] <= intervals[i][1]:
            res[0][0] = min(res[0][0],intervals[i][0])
            res[0][1] = max(res[0][1],intervals[i][1])
        else:
            res.insert(0,intervals[i])
    return res

# inter =  [[1,3],[2,6],[6,11],[8,10],[15,18]]

# inter =  [[1,3],[2,6],[8,10],[6,11],[15,18]]
# inter = []
# inter = [[1,4],[0,4]]
# inter = [[2,3],[4,5],[6,7],[8,9],[1,10]]
inter = [[1,3],[2,6],[8,10],[15,18]]
merge(inter)



