#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        arr_length = len(arr)

        if arr_length in [0, 1, 2] or arr[0] >= arr[1]:
            return False
        
        # max_val = arr[0]
        # peak = False
        # for i in range(1, len(arr)-1):
        #     if arr[i] > max_val:
        #         max_val = arr[i]
        #         peak = True
        #     elif arr[i] < max_val and arr[i] < arr[i-1] and peak:
        #         continue
        #     else:
        #         return False
        # if arr[arr_length-1] >= arr[arr_length-2]:
        #     return False
        # return True

        down = False
        for i in range(arr_length-1):
            if arr[i] > arr[i+1]:
                down = True
            elif (arr[i] < arr[i+1] and down) or arr[i] == arr[i+1]:
                return False
        return down

        

            
            
        
# @lc code=end

