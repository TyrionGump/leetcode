--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
# Write your MySQL query statement below
SELECT e.Name AS `Employee`
FROM Employee AS e
INNER JOIN Employee AS m
ON e.ManagerID = m.ID
WHERE e.Salary > m.Salary;
-- @lc code=end

