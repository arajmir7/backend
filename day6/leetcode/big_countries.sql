-- 1. Create the 'World' table (Schema)
CREATE TABLE World (
    name VARCHAR(255),
    continent VARCHAR(255),
    area INT,
    population INT,
    gdp BIGINT
);

-- 2. Insert the data (Seed Data from LeetCode example)
INSERT INTO World (name, continent, area, population, gdp) VALUES 
('Afghanistan', 'Asia', 652230, 25500100, 20343000000),
('Albania', 'Europe', 28748, 2831741, 12960000000),
('Algeria', 'Africa', 2381741, 37100000, 188681000000),
('Andorra', 'Europe', 468, 78115, 3712000000),
('Angola', 'Africa', 1246700, 20609294, 100990000000);

-- 3. YOUR SOLUTION (The Query)
SELECT name, population, area
FROM World
WHERE area >= 3000000 N
   OR population >= 25000000;