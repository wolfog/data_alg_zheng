'''
Author: rudy
Date: 2022-03-14 13:58:03
LastEditTime: 2022-03-14 17:32:42
Description: 争哥的算法训练营第二期
'''


# 定义的节点类
from typing import List


class ListNode:
    def __init__(self, value=None, next_node=None):
        # 这样使用有两个好处，一个是代码惯列，另一个是如果这里写成self.value  会直接调用setter 方法，这样会直接导致递归超出python限制。
        self._value = value
        self._next_node = next_node
    # property 使得将方法当成属性使用。
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            self._value = value
        else:
            print("value should be int")

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        if isinstance(next_node, ListNode):
            self._next_node = next_node
        else:
            print("next should be ListNode")


class Solution:

    # 删除指定值的节点。
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tp_node = head
        # 空链表，首节点，尾节点特殊情况处理，这些特殊情况能否使用哨兵节点，快慢指针，头尾指针解决。
        gd_node = ListNode()  # 哨兵节点。
        gd_node.next_node = tp_node
        tp_node.next_node = gd_node
        while tp_node.next_node != None:
            if tp_node.next_node.value == val:
                tp_node.next_node = tp_node.next_node.next_node
            else:
                tp_node = tp_node.next_node

        return head.next_node


if __name__ == "__main__":
    slutn = Solution()
    slutn.removeElements(ListNode(), 2)
