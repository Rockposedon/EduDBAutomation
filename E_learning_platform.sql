create database E_learning;
use E_learning;
CREATE TABLE User (
user_id VARCHAR(10) NOT NULL PRIMARY KEY,
f_name VARCHAR(30) NOT NULL,
l_name VARCHAR(30) NOT NULL,
email VARCHAR(50) NOT NULL,
mobile VARCHAR(100),
address VARCHAR(100),
password VARCHAR(30) NOT NULL,
registration_date DATE
);

CREATE TABLE Instructor (
instructor_id INT AUTO_INCREMENT PRIMARY KEY,
user_id VARCHAR(10) NOT NULL UNIQUE,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE Course (
course_id INT AUTO_INCREMENT PRIMARY KEY,
instructor_id INT NOT NULL,
user_id VARCHAR(10) NOT NULL UNIQUE,
course_title VARCHAR(100) NOT NULL,
level ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL,
fee DECIMAL(10, 2) NOT NULL,
duration INT NOT NULL,
FOREIGN KEY (instructor_id) REFERENCES Instructor(instructor_id),
FOREIGN KEY (user_id) REFERENCES User(user_id));


CREATE TABLE Payment (
payment_id INT AUTO_INCREMENT PRIMARY KEY,
user_id VARCHAR(10) NOT NULL,
course_id INT NOT NULL,
payment_date DATE NOT NULL,
amount DECIMAL(10, 2) NOT NULL,
payment_status ENUM('Pending', 'Completed') NOT NULL,
FOREIGN KEY (user_id) REFERENCES User(user_id),
FOREIGN KEY (course_id) REFERENCES Course(course_id)
);


CREATE TABLE Test (
test_id INT AUTO_INCREMENT PRIMARY KEY,
user_id VARCHAR(10) NOT NULL,
course_id INT NOT NULL,
test_name VARCHAR(100) NOT NULL,
test_date DATE NOT NULL,
max_score INT NOT NULL,
FOREIGN KEY (user_id) REFERENCES User(user_id),
FOREIGN KEY (course_id) REFERENCES Course(course_id)
);


CREATE TABLE Feedback (
feedback_id INT AUTO_INCREMENT PRIMARY KEY,
user_id VARCHAR(10) NOT NULL,
course_id INT NOT NULL,
rating DECIMAL(3, 2) NOT NULL,
feedback_date DATE NOT NULL,
FOREIGN KEY (user_id) REFERENCES User(user_id),
FOREIGN KEY (course_id) REFERENCES Course(course_id)
);