--
-- @lc app=leetcode id=185 lang=mysql
--
-- [185] Department Top Three Salaries
--

-- @lc code=start
# Write your MySQL query statement below
-- Notice that columns not in from cannot be used after where.
SELECT D.Name AS `Department`, RE.Name AS `Employee`, RE.Salary 
FROM (
    SELECT *, Dense_RANK() OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) AS RankInDept
    FROM Employee
) AS RE
INNER JOIN Department AS D
on RE.DepartmentId = D.Id
WHERE RE.RankInDept <= 3;

-- Wihout subquery. For each employee find how many employees having higher 
-- salary than him or her.
-- SELECT D.Name AS `Department`, E1.Name AS `Employee`, E1.Salary
-- FROM Department AS D, Employee AS E1, Employee AS E2
-- WHERE D.Id = E1.DepartmentId
-- AND E1.DepartmentId = E2.DepartmentId
-- AND E1.Salary <= E2.Salary
-- GROUP BY D.Id, E1.Id
-- HAVING COUNT(DISTINCT E2.Salary) <= 3;

-- @lc code=end

