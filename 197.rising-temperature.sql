--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
# Write your MySQL query statement below

-- If you use DAY(), there is a problem that the difference of year may be not 1,
-- but the difference of day is 1. This cannot represent yesterday.
-- SELECT W2.id
-- FROM Weather AS W1
-- INNER JOIN Weather AS W2
-- ON TO_DAYS(W2.recordDate) - TO_DAYS(W1.recordDate) = 1
-- AND W2.Temperature > W1.Temperature;

SELECT W2.id
FROM Weather AS W1
INNER JOIN Weather AS W2
ON SUBDATE(W2.recordDate, 1) = W1.recordDate
AND W2.Temperature > W1.Temperature;

-- @lc code=end

