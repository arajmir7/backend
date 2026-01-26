-- Weather Observation Station 3
-- Select distinct city names where ID is even

-- 1. Create table
CREATE TABLE STATION (
    ID INT,
    CITY VARCHAR(21),
    STATE VARCHAR(2),
    LAT_N FLOAT,
    LONG_W FLOAT
);

-- 2. Insert sample data (you can tweak/add more)
INSERT INTO STATION VALUES
(1, 'New York', 'NY', 40.71, 74.00),
(2, 'Los Angeles', 'CA', 34.05, 118.24),
(3, 'Chicago', 'IL', 41.87, 87.62),
(4, 'Houston', 'TX', 29.76, 95.36),
(6, 'Los Angeles', 'CA', 34.05, 118.24);

-- 3. Solution query
SELECT DISTINCT CITY
FROM STATION
WHERE ID % 2 = 0;
