#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits

        cur = len(digits) - 1

        while (cur >= -1):
            if cur == -1:
                digits.insert(0, 1)
                return digits
            if digits[cur] + 1 < 10:
                digits[cur] += 1
                return digits
            else:
                digits[cur] = 0
            cur -= 1

        
# @lc code=end

