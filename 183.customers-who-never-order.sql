--
-- @lc app=leetcode id=183 lang=mysql
--
-- [183] Customers Who Never Order
--

-- @lc code=start
# Write your MySQL query statement below
SELECT Name AS Customers
FROM Customers
LEFT JOIN Orders
ON Customers.ID = Orders.CustomerID
WHERE Orders.CustomerID IS NULL;
-- @lc code=end

