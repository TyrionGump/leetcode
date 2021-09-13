--
-- @lc app=leetcode id=180 lang=mysql
--
-- [180] Consecutive Numbers
--

-- @lc code=start
# Write your MySQL query statement below
SELECT DISTINCT Num AS ConsecutiveNums
FROM Logs
WHERE (ID+1, Num) IN (
    SELECT * FROM Logs
    ) AND (ID+2, Num) IN (
        SELECT * FROM Logs
    );


-- @lc code=end

