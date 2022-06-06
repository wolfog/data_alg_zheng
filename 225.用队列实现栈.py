#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用两个队列实现栈
#

# 对列 ：先进先出。尾插头出。栈：先进后出，尾插尾出
#
#
# @lc code=start
class MyStack:

    def __init__(self):
        self.left_queue = []


    def push(self, x: int) -> None:
        if len(self.left_queue)==0: 
            self.left_queue.append(x)
        else:
            rigth_queue = self.left_queue
            self.left_queue = [x]
            self.left_queue.extend(rigth_queue)
            rigth_queue = None


    def pop(self) -> int: # 出栈(对列pip 对头元素)
        return  -1 if len(self.left_queue) ==0 else self.left_queue.pop(0)


    def top(self) -> int:# 返回栈顶元素
        return self.left_queue[0]


    def empty(self) -> bool: # 栈是否为空
        return False if len(self.left_queue)>0 else True



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

