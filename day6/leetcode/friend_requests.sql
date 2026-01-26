-- 1. Schema Provisioning
CREATE TABLE FriendRequest (
    sender_id INT,
    send_to_id INT,
    request_date DATE
);

CREATE TABLE RequestAccepted (
    requester_id INT,
    accepter_id INT,
    accept_date DATE
);

-- 2. Data Seeding (Simulating the social funnel)
INSERT INTO FriendRequest (sender_id, send_to_id, request_date) VALUES 
(1, 2, '2016-06-01'), (1, 3, '2016-06-01'), (1, 4, '2016-06-01'), 
(2, 3, '2016-06-02'), (3, 4, '2016-06-09');

INSERT INTO RequestAccepted (requester_id, accepter_id, accept_date) VALUES 
(1, 2, '2016-06-03'), (1, 3, '2016-06-08'), (2, 3, '2016-06-08'), 
(3, 4, '2016-06-09'), (3, 4, '2016-06-10');

-- 3. THE SOLUTION (Strategic Metric Extraction)
-- We cast to FLOAT to ensure the division doesn't return a boring integer
SELECT 
    ROUND(
        IFNULL(
            -- Use 1.0 * to force float division in SQLite/MySQL
            1.0 * (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) AS a) / 
            NULLIF((SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) AS r), 0), 
            0
        ), 
    2) AS accept_rate;