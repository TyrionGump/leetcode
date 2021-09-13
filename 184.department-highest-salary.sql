--
-- @lc app=leetcode id=184 lang=mysql
--
-- [184] Department Highest Salary
--

-- @lc code=start
# Write your MySQL query statement below
-- SELECT DepartmentStats.DepartmenName AS `Department`, Employee.Name AS `Employee`, Employee.Salary AS `Salary`
-- FROM (
--     SELECT Employee.DepartmentId, Department.Name AS `DepartmenName`, MAX(Employee.Salary) AS `DepartmentMaxSalary`
--     FROM Employee
--     INNER JOIN Department
--     ON Employee.DepartmentId = Department.Id
--     GROUP BY Department.Id
    
-- ) AS DepartmentStats
-- INNER JOIN Employee
-- ON Employee.DepartmentId = DepartmentStats.DepartmentId
-- WHERE Employee.Salary = DepartmentStats.DepartmentMaxSalary;

-- Notice: Alias only work for query **executed** behind the alias.
-- SELECT dep.Name AS `Department`, emp.Name AS `Employee`, emp.Salary
-- FROM Employee AS emp
-- INNER JOIN Department AS dep ON emp.DepartmentId = dep.Id
-- WHERE (emp.DepartmentId, Salary) IN(
--     SELECT DepartmentId, MAX(Salary)
--     FROM Employee
--     GROUP BY DepartmentId
-- );

SELECT dep.Name AS `Department`, emp.Name AS `Employee`, emp.Salary
FROM Employee AS emp
INNER JOIN Department AS dep ON emp.DepartmentId = dep.Id
INNER JOIN (
    SELECT DepartmentId, MAX(Salary) AS DepartmentMaxSalary
    FROM Employee
    GROUP BY DepartmentId
) AS DepartmentStats ON DepartmentStats.DepartmentId = emp.DepartmentId
WHERE emp.Salary = DepartmentStats.DepartmentMaxSalary;
-- @lc code=end

