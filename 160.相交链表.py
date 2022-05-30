#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def  reverseLinkedlist(self ,head):
        # 链表翻转，并且返回链表的长度。
        node_nums = 0
        temp_node  = head
        while temp_node:
            node_nums+=1
            temp_save = temp_node.next
            temp_node.next = head
            head = temp_node
            temp_node = temp_save.next
        return head,node_nums

    def m1(self,headA,headB):
        # 思路：目前能想到比较暴力的就是暴力搜索判断b中的节点等于a中的某个节点（id 是否相等）
        # 时间复杂度0(n*m),空间复杂度是0（1)
        tempa,tempb = headA,headB
        while tempa:
            while tempb:
                if id(tempa) == id(tempb):
                    return tempa
                tempb = tempb.next
            tempa  = tempa.next
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 这里有个简单前提条件，就是两个链表一旦有相同的节点，后面的节点就都一样

        if 0:
            return self.m1(headA,headB)

        # 将两个链表倒序（记录下链表的长度），然后如果next 不相同的节点（当前下标是num)，就是
        # 倒数第num个是需要返回的。 然后在将链表倒序（恢复如初），在遍历短的链表当是（short-num)
        # 返回这个节点就可以。时间复杂度（0（n+m)。空间复杂度是o(1)

        elif 1:
            headA, a_node_nums = self.reverseLinkedlist(headA)
            headB, b_node_nums = self.reverseLinkedlist(headB)
            a_temp_node, b_temp_node = headA, headB
            last_same_index = -1
            for i in range(min(a_node_nums, b_node_nums)):
                if id(a_temp_node.next) != id(b_temp_node):
                    break
                last_same_index += 1
            if last_same_index==-1:
                return None
            # 经过上次循环之后，就已经确定了相同节点的倒数下标。
            headA, a_node_nums = self.reverseLinkedlist(headA)
            headB, b_node_nums = self.reverseLinkedlist(headB)
            # 遍历len(a)-last_same_index 次，返回这个节点
            a1_temp_node = headA
            for i in range(a_node_nums-last_same_index):
                a1_temp_node = a1_temp_node.next
            return a1_temp_node
        else:           
            pass
        # 学习到别人的思路：如果两个链表有相交，那么就去逐个比较min(len(a),len(b))元素，时间复杂度就是
        # o(n+m),空间复杂度是0(1）

        
# @lc code=end

