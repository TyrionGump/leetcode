#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
             return False

        pattern_to_word = {}
        word_to_pattern = {}

        for idx, letter in enumerate(pattern):
            word = words[idx]
        
            # Check pattern -> word mapping
            if letter in pattern_to_word:
                if pattern_to_word[letter] != word:
                    return False
            else:
                pattern_to_word[letter] = word

            # Check word -> pattern mapping
            if word in word_to_pattern:
                if word_to_pattern[word] != letter:
                    return False
            else:
                word_to_pattern[word] = letter
    
        
        return True
        # s = s.split()

        # return (len(set(pattern)) ==
        #         len(set(s)) ==
        #         len(set(zip_longest(pattern,s))))
        
        
# @lc code=end

