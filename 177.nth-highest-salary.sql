--
-- @lc app=leetcode id=177 lang=mysql
--
-- [177] Nth Highest Salary
--

-- @lc code=start
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL((
        SELECT DISTINCT Salary
        FROM (
          SELECT Salary, DENSE_RANK() OVER(ORDER BY Salary DESC) AS SRank
          FROM Employee
        ) AS SalaryRank
        WHERE SRank = N
      ), NULL)
  );
END
-- @lc code=end

