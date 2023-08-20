#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        
        first = self.out_stack.pop()

        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
        
        return first

    def peek(self) -> int:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        
        first = self.out_stack[-1]

        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
        
        return first
        

    def empty(self) -> bool:
        return not self.in_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

