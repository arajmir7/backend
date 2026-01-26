-- 1. Schema Creation based on leetcode description
CREATE TABLE Stadium (
    id INT,
    visit_date DATE,
    people INT
);

-- 2. Data Seeding (from Example 1)
INSERT INTO Stadium (id, visit_date, people) VALUES 
(1, '2017-01-01', 10),
(2, '2017-01-02', 109),
(3, '2017-01-03', 150),
(4, '2017-01-04', 99),
(5, '2017-01-05', 145),
(6, '2017-01-06', 1455),
(7, '2017-01-07', 199),
(8, '2017-01-09', 188);

-- 3. YOUR SOLUTION
WITH filtered AS (
    SELECT id, visit_date, people
    FROM Stadium
    WHERE people >= 100
),
grouped AS (
    SELECT *,
           id - ROW_NUMBER() OVER(ORDER BY id) as grp
    FROM filtered
)
SELECT id, visit_date, people
FROM grouped
WHERE grp IN (
    SELECT grp
    FROM grouped
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;