--
-- @lc app=leetcode id=262 lang=mysql
--
-- [262] Trips and Users
--

-- @lc code=start
# Write your MySQL query statement below

-- -- Firstly, find the count of cancelled requests for each date
-- SELECT Request_at, COUNT(CASE
--                         WHEN Trips.Status = 'cancelled_by_driver' THEN 1
--                         ELSE NULL
--                         END) AS CancelledOrderCount
-- FROM Trips
-- WHERE Request_at BETWEEN '2013-10-01' AND '2013-10-03'
-- GROUP BY Request_at;

-- Secondly, find the count of unbanned requests for each date
SELECT Request_at AS `Day`, 
        ROUND(COUNT(IF(Trips.Status LIKE 'cancelled%', 1, NULL)) / COUNT(Id), 2) AS `Cancellation Rate`
FROM Trips
JOIN Users AS Client ON Client_Id = Client.Users_Id
JOIN Users AS Driver ON Driver_Id = Driver.Users_Id
WHERE Client.Banned = 'No' 
AND Driver.Banned = 'No'
AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at;


-- @lc code=end

