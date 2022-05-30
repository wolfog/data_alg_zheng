#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 最简单的思路：先遍历一遍，知道总共有几个元素，再次遍历等到倒数n-1的时候操作,也就是len(head)-n-1。
        # 为了预防只有一个节点的情况，所以给链表头插一个哨兵节点
        guard = ListNode(-1,head)
        head = guard
        temp_node = head
        nodes = 0
        while temp_node:
            nodes+=1
            temp_node = temp_node.next
        temp_node1 = head
        for index  in range(nodes):
            if index==nodes-n-1: #倒数n-1个节点：
                temp_node1.next = temp_node1.next.next
                break
            temp_node1 = temp_node1.next
        return head.next

# @lc code=end

