--
-- @lc app=leetcode id=176 lang=mysql
--
-- [176] Second Highest Salary
--

-- @lc code=start
-- -- Wrong answer for only one row in the database also If we only have two largest number.
-- SELECT IFNULL((SELECT Salary As SecondHighestSalary
-- FROM Employee
-- ORDER BY Salary DESC
-- LIMIT 1, 1;), NULL)


-- SELECT MAX(Salary) AS SecondHighestSalary
-- FROM Employee
-- WHERE Salary < (
--     SELECT MAX(Salary)
--     FROM Employee
-- );

-- Notice the IFNULL and DISTINCT
SELECT IFNULL((SELECT DISTINCT Salary
FROM (
    SELECT Salary, DENSE_RANK() OVER(ORDER BY Salary DESC) AS s_rank
    FROM Employee) 
    AS Salary_Rank
    WHERE Salary_Rank.s_rank = 2), NULL) AS SecondHighestSalary;
-- @lc code=end

