#
# @lc app=leetcode id=193 lang=bash
#
# [193] Valid Phone Numbers
#

# @lc code=start
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
# @lc code=end

