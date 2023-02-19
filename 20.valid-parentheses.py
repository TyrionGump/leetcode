#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # rigth_to_left_brackets = {")": "(", "]": "[", "}": "{"}
        # right_brackets = rigth_to_left_brackets.keys()
        # left_brackets = rigth_to_left_brackets.values()

        # stack = []

        # for bracket in s:
        #     if bracket in left_brackets:
        #         stack.append(bracket)
        #     elif bracket in right_brackets:
        #         # Check whether stack is empty since only right brackets are there and the stack is empty. 
        #         if stack and stack[-1] == rigth_to_left_brackets[bracket]:
        #             stack.pop()
        #         else:
        #             return False
        
        # return not stack

        rigth_to_left_brackets = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for bracket in s:
            if bracket in rigth_to_left_brackets:
                stack.append(bracket)
            elif not stack or rigth_to_left_brackets[stack.pop()] != bracket:
                return False
        
        return not stack


# @lc code=end

