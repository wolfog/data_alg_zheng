'''
Author: rudy
LastEditors: rudy
Date: 2022-06-02 16:18:40
LastEditTime: 2022-06-02 18:29:08
Description: 两个栈实现队列。入队，什么都不返回；出队，返回元素。
思路： 初始化两个栈（用列表实现）
>1. 入队，正常添加；出队，将所有元素转移到另外一个栈中，最后一个元素出栈
>2. 添加的时候就放好顺序，直接出。
'''

class CQueue:
    
    def __init__(self):  # 
        self.left_stack = []  # 只能栈顶入，栈顶出。放到list中就是只允许操作-1 位置的元素。


    
    def appendTail(self, value: int) -> None:
        if len(self.left_stack)==0: 
            self.left_stack.append(value)
        else:
            rigth_stack = self.left_stack
            self.left_stack = [value]
            self.left_stack.extend(rigth_stack)
            rigth_stack = None


    def deleteHead(self) -> int:
        return self.left_stack.pop() if len(self.left_stack)==0 else -1
        
        
            


