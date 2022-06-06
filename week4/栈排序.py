'''
Author: rudy
LastEditors: rudy
Date: 2022-06-02 18:50:50
LastEditTime: 2022-06-02 20:24:46
Description:  编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操
作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。
# 个人理解：在插入的时候，就确保最小元素位于栈顶. 个人感觉这个理解不正确。如果只是让最小的元素位于栈顶，那么最小元素出栈的之后，又需要重新排列。
# 思路： 两个栈：在添加的时候，判断元素与栈顶元素的大小，如果小于栈顶元素，直接入栈；如果大于栈顶，栈顶元素出栈，进入临时栈中，继续循环。
# 为啥呢：时间和空间都使用非常大。
'''
class SortedStack:
    
    # 递归的构建函数
    # def __init__(self):
    #     self.stack = []
    #     # 使用递归的时候，不使用栈也可以，一个变量就可以解决问题。
    #     # self.temp_stack = [] # 到底是栈还是其他数据结构，区别就在与栈只能在末尾添加，末尾pop .而list 却可以随意操作。所以只要限制其操作下标为-1 就行了

    # 递归
    # def push(self, val: int) -> None:
    #     if self.isEmpty():
    #         self.stack.append(val)
    #     else:
    #         if val > self.peek(): # 大于栈顶，出栈，然后继续调用push 方法（使用递归）.在使用递归的时候：最内侧的
    #         # 局部变量不影响外侧的局部变量。但是如果是全局变量、成员变量是会影响。这就是一个变量作用域的问题
    #             pop_val = self.stack.pop()
    #             self.push(val)
    #             self.stack.append(pop_val)
    #         else:
    #             self.stack.append(val)

    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def push(self, val: int) -> None:
        if self.isEmpty():
            self.stack.append(val)
        else:
            while self.peek()>=0 and val>self.peek():
                # 如果大于
                self.temp_stack.append(self.stack.pop())
            self.stack.append(val)
            while len(self.temp_stack):# 有元素的话，就一直继续
                self.stack.append(self.temp_stack.pop())


    def pop(self) -> None:
        if not self.isEmpty():
            self.stack.pop()


    def peek(self) -> int:
        return -1 if self.isEmpty() else self.stack[-1]


    def isEmpty(self) -> bool:
        return not bool(len(self.stack))



if __name__ == "__main__":
   ss = SortedStack()
   ss.push(1)
   ss.push(2)