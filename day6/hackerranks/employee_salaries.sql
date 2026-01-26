-- Employee Salaries (local practice)

CREATE TABLE Employee (
    employee_id INT,
    name VARCHAR(50),
    months INT,
    salary INT
);

INSERT INTO Employee VALUES
(1, 'Alice', 5, 3000),
(2, 'Bob', 12, 4000),
(3, 'Charlie', 7, 2500),
(4, 'David', 3, 1800),
(5, 'Eve', 9, 2200);

SELECT name
FROM Employee
WHERE salary > 2000
  AND months < 10
ORDER BY employee_id;
