#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 判断链表是否是否有环，用快慢指针，快的走2步，慢的走1步。如果快的等于慢的，就说明有环
        head = ListNode(-1,head)
        # 还有一点需要牢记：slow指向哨兵节点，fast指向头结点的下一个节点。如果相反，当进行一次循环之后，两者肯定会指向第2（start from index 0）个节点。
        # 就永远返回true
        slow,fast  = head,head.next
        # 循环结束
        while fast  and fast.next:
            # 无论如何都会返回True,因为刚一开始的确都是指向头节点都相等。后添加了哨兵节点。
            if fast is slow: #等价于id(a)==id(b)
                return True
            fast = fast.next.next
            slow = slow.next
        return False


        
# @lc code=end

