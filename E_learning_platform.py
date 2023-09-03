import mysql.connector
from faker import Faker
import random

fake = Faker()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="E_learning"
)

cursor = conn.cursor()

# Generate 50 users
for _ in range(50):
    user_id = fake.unique.random_int(min=100, max=999)
    f_name = fake.first_name()
    l_name = fake.last_name()
    email = f"{f_name.lower()}.{l_name.lower()}@example.com"
    mobile = str(fake.random_int(min=1000000000, max=9999999999))
    address = fake.address()
    password = fake.password()
    registration_date = fake.date_this_decade()
    
    cursor.execute("INSERT INTO User (user_id, f_name, l_name, email, mobile, address, password, registration_date) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (user_id, f_name, l_name, email, mobile, address, password, registration_date))

# Generate 50 instructors

for user_id in range(1, 51):
    instructor_id = user_id + 1000
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    cursor.execute("INSERT INTO Instructor (instructor_id, user_id, first_name, last_name) "
                   "VALUES (%s, %s, %s, %s)",
                   (instructor_id, user_id, first_name, last_name))

# Generate 50 courses
for _ in range(50):
    course_id = fake.unique.random_int(min=2001, max=3000)
    instructor_id = fake.random_int(min=1001, max=2000)  # Using instructor_id from the generated instructors
    course_title = fake.catch_phrase()
    level = random.choice(['Beginner', 'Intermediate', 'Advanced'])
    fee = round(random.uniform(10, 200), 2)
    duration = fake.random_int(min=1, max=12)
    
    cursor.execute("INSERT INTO Course (course_id, instructor_id, course_title, level, fee, start_date, end_date, duration) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (course_id, instructor_id, course_title, level, fee, fake.date_this_decade(), fake.date_this_decade(), duration))

# Generate 50 payments
for _ in range(50):
    payment_id = fake.unique.random_int(min=3001, max=4000)
    user_id = fake.random_int(min=100, max=999)  # Using user_id from the generated users
    course_id = fake.random_int(min=2001, max=3000)  # Using course_id from the generated courses
    payment_date = fake.date_this_year()
    amount = round(random.uniform(10, 100), 2)
    payment_status = random.choice(['Pending', 'Completed'])
    
    cursor.execute("INSERT INTO Payment (payment_id, user_id, course_id, payment_date, amount, payment_status) "
                   "VALUES (%s, %s, %s, %s, %s, %s)",
                   (payment_id, user_id, course_id, payment_date, amount, payment_status))

# Generate 50 tests
for _ in range(50):
    test_id = fake.unique.random_int(min=4001, max=5000)
    user_id = fake.random_int(min=100, max=999)  # Using user_id from the generated users
    course_id = fake.random_int(min=2001, max=3000)  # Using course_id from the generated courses
    test_name = fake.catch_phrase()
    test_date = fake.future_date(end_date='+1y')
    max_score = fake.random_int(min=10, max=50)
    
    cursor.execute("INSERT INTO Test (test_id, user_id, course_id, test_name, test_date, max_score) "
                   "VALUES (%s, %s, %s, %s, %s, %s)",
                   (test_id, user_id, course_id, test_name, test_date, max_score))

# Generate 50 feedbacks
for _ in range(50):
    feedback_id = fake.unique.random_int(min=5001, max=6000)
    user_id = fake.random_int(min=100, max=999)  # Using user_id from the generated users
    course_id = fake.random_int(min=2001, max=3000)  # Using course_id from the generated courses
    rating = round(random.uniform(1, 5), 2)
    feedback_date = fake.date_this_year()
    
    cursor.execute("INSERT INTO Feedback (feedback_id, user_id, course_id, rating, feedback_date) "
                   "VALUES (%s, %s, %s, %s, %s)",
                   (feedback_id, user_id, course_id, rating, feedback_date))

conn.commit()
conn.close()

print("Data inserted successfully.")
