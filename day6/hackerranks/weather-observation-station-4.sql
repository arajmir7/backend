-- Find difference between total CITY entries and distinct CITY entries

SELECT 
    COUNT(CITY) - COUNT(DISTINCT CITY) AS city_difference
FROM STATION;
