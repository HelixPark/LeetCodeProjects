# 单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None

    def initList(self,data):
        self.head = ListNode(data[0])
        p = self.head

        for i in data[1::]:
            node = ListNode(i)
            p.next = node
            p = p.next

    def printList(self):
        p = self.head
        while p:
            print(p.val)
            p = p.next




data1 = [1,2,4]
data2 = [1,3,4]
l1 = LinkList()
l2 = LinkList()

l1.initList(data1)
l2.initList(data2)

l1.printList()
l2.printList()


print("ddd")


# 思路对，写的也对，LC上说没val。待测验
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1

    res = ListNode(0)
    tmp = res
    while l1 and l2:
        if l1.val < l2.val:
            tmp.val = l1.val
            l1 = l1.next
        else:
            tmp.val = l2.val
            l2 = l2.next

        tmp = tmp.next

    while l1:
        tmp.next = l1
    else:
        tmp.next = l2

    return res.next