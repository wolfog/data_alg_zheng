'''
Author: rudy
Date: 2022-04-26 19:00:37
LastEditTime: 2022-05-20 09:53:56
Description: file content(链表练习题)
'''
from json.tool import main


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1,l2):
        # 解释：
        guard = ListNode(0) #  建哨兵节点
        # 修改1：end = guard.next 这接这样写，就没法跟while 里面的节点链接起来。
        end = guard # 尾巴指针也指向这个节点
        head = guard # 头指针直线这个节点 。前面是标准写法。
        carry = 0
        while l1 or l2:
            v1,v2 = 0,0
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val
            sum_temp = v1+v2+carry
            carry = sum_temp//10
            remainder = sum_temp%10
            # 修改2：end = ListNode(remainder)
            end.next = ListNode(remainder)
            end  = end.next
            if l1:
                l1 = l1.next
            if l2 :
                l2 = l2.next
        if carry: # carry 不为0 才
            # 修改3：end = ListNode(carry)
            end.next = ListNode(carry)
        return head.next
            
if __name__ == "__main__":
       a = ListNode(2)
       print(a)
       print(type(a))
        


