import psycopg2
from datetime import datetime

# Database connection parameters
db_params = {
    'host': 'localhost',
    'database': 'MyC',
    'user': 'postgres',
    'password': '5tgb%TGB',
    'port': '5432'
}

# Connect to the database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Read data from the text file
with open('formData.txt', 'r') as file:
    lines = file.readlines()

# Process each line and insert into the database
for line in lines:
    # Split the line into individual fields
    fields = line.strip().split(',')

    # Extract data
    date_str, wake_up, breakfast, study, lunch, exercise, shower, dinner, sleep = fields

    # Convert date string to datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')


    # Insert data into the database
    cursor.execute(
    """
    INSERT INTO schedule (date, wake_up, breakfast, study, lunch, exercise, shower, dinner, sleep)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (date) DO UPDATE
    SET
        wake_up = COALESCE(EXCLUDED.wake_up, schedule.wake_up),
        breakfast = COALESCE(EXCLUDED.breakfast, schedule.breakfast),
        study = COALESCE(EXCLUDED.study, schedule.study),
        lunch = COALESCE(EXCLUDED.lunch, schedule.lunch),
        exercise = COALESCE(EXCLUDED.exercise, schedule.exercise),
        shower = COALESCE(EXCLUDED.shower, schedule.shower),
        dinner = COALESCE(EXCLUDED.dinner, schedule.dinner),
        sleep = COALESCE(EXCLUDED.sleep, schedule.sleep);
    """,
    (
        date,
        wake_up if wake_up else None,
        breakfast if breakfast else None,
        study if study else None,
        lunch if lunch else None,
        exercise if exercise else None,
        shower if shower else None,
        dinner if dinner else None,
        sleep if sleep else None,
    ),
)



# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()
