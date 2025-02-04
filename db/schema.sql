CREATE DATABASE IF NOT EXISTS taskdb;

USE taskdb;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    priority ENUM('low', 'medium', 'high') DEFAULT 'low',
    due_date DATETIME NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert example tasks
INSERT INTO tasks (title, description, priority, due_date)
VALUES 
('Task 1', 'Description for task 1', 'high', NOW() + INTERVAL 1 DAY),
('Task 2', 'Description for task 2', 'medium', NOW() + INTERVAL 3 DAY),
('Task 3', 'Description for task 3', 'low', NOW() + INTERVAL 7 DAY);
