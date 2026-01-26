-- 1. Reset the table for a clean run
DROP TABLE IF EXISTS Courses;

-- 2. Create the 'Courses' table
CREATE TABLE Courses (
    student VARCHAR(255),
    class VARCHAR(255)
);

-- 3. Insert the sample data
INSERT INTO Courses (student, class) VALUES 
('A', 'Math'), ('B', 'English'), ('C', 'Math'), 
('D', 'Biology'), ('E', 'Math'), ('F', 'Computer'), 
('G', 'Math'), ('H', 'Math'), ('I', 'Math');

-- 4. YOUR SOLUTION
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;