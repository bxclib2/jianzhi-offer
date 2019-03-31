# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 输入一个链表，输出该链表中倒数第k个结点。
# 注意判断前两个特殊用例
class Solution:
    def FindKthToTail(self, head, k):
        if not head or k == 0:
            return 
        first = head
        second = head
        for i in range(k-1):
            second = second.next
            if second is None:
                return 
            

        while second.next is not None:
            second =  second.next
            first = first.next
        return first
            
