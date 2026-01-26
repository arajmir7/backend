-- 1. Schema Provisioning
CREATE TABLE RequestAccepted2 (
    requester_id INT,
    accepter_id INT,
    accept_date DATE
);

SELECT id, COUNT(*) AS num
FROM (
    -- Reference your existing table's requester column
    SELECT requester_id AS id FROM RequestAccepted2
    UNION ALL
    -- Reference your existing table's accepter column
    SELECT accepter_id AS id FROM RequestAccepted2
) AS all_friends
GROUP BY id
ORDER BY num DESC
LIMIT 1;

-- 2. Data Seeding (from Example 1)
INSERT INTO RequestAccepted2 (requester_id, accepter_id, accept_date) VALUES 
(1, 2, '2016-06-03'),
(1, 3, '2016-06-08'),
(2, 3, '2016-06-08'),
(3, 4, '2016-06-09');

-- 3. YOUR SOLUTION
SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted2
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted2
) AS all_ids
GROUP BY id
ORDER BY num DESC
LIMIT 1;