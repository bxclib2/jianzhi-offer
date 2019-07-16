# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == []:
            return []
        if len(lists)%2!=0:
            lists.append(None)

        while len(lists)>1:
            if len(lists)%2!=0:
                lists.append(None)
            list_temp = []
            for i,j in zip(lists[::2],lists[1::2]):
                list_temp.append(self.mergeTwoLists(i,j))
            lists = list_temp
            #print (len(lists))
        return lists[0]
            
            

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        start = res
        while (l1 is not None) and (l2 is not None):
            if l1.val<l2.val:
                res.next = ListNode(l1.val)
                l1 = l1.next
                res = res.next
            else:
                res.next = ListNode(l2.val)
                res = res.next
                l2 = l2.next
        if l1 is None:
            res.next = l2
        else:
            res.next = l1
        return start.next
