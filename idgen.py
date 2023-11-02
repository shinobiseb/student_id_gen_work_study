import random  # Import the random module

import pyperclip as pc
import csv

user = "Seb"

# data_str = "33732082\t1212\t1\tF"
# pc.copy(data_str)

# Function to generate a random number within a range
def random_num(minimum, maximum):
    return random.randint(minimum, maximum)

# Function to generate a random academic term
def random_term():
    season_num = [2, 6, 9]
    return 1000 + (random_num(19, 22) * 10) + random.choice(season_num)

# Function to generate a random session
def random_sess():
    sessions = [1, 1, 1, 1, 1, 'WIN']
    return random.choice(sessions)

# List of passing grades
passing_grades = [
    'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'P', 'S', 'CR'
]

# List of failing grades
failing_grades = [
    'F', 'FIN'
]

def is_failing_grade(grade):
    return grade in failing_grades

# Function to generate a random grade
def grade_gen():
    num = random_num(1, 2)
    if num == 1:
        return random.choice(passing_grades)
    elif num == 2:
        return random.choice(failing_grades)
    else:
        return "invalid Grade Gen"
    
subjects = [
    "ENG",
    "MAT",
    "PSY",
    "SOC",
    "COM",
    "CSC",
    "CSC",
    "MAT",
    "PSY",
    "MAT",
    "ENG",
    "ENG",
    "MAT",
    "ENG",
    "PSY",
    "COM",
    "BIO",
    "CHE",
    "ENG",
    "MAT",
    "MAT",
    "POL",
    "MAT",
    "PHY",
    "MAT",
    "PSY",
    "BIO",
    "ENG",
    "PSY",
    "BIO",
    "ENG",
    "ENG",
    "MAT",
    "PSY",
    "PHY",
    "ENG",
    "MAT",
    "CHE",
    "VPA",
    "HIS",
    "BIO",
    "MAT",
    "CSC",
    "MAT",
    "BIO",
    "HIS",
    "LAC",
    "WGS",
    "SPA",
    "HUM",
]

new_subject_arr = []

def sort_subjects():
    for subject in subjects:
        if subject not in new_subject_arr:
            new_subject_arr.append(subject)

sort_subjects()

def random_subject():
    return random.choice(new_subject_arr)

def create_and_write_to_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t') 
        for _ in range(6):
            student_id = str(random_num(10000000, 99999999))
            has_failing_grade = False

            for _ in range(4):
                row = [
                    student_id,
                    str(random_term()),
                    str(random_sess()),
                    grade_gen(),
                    str(random_subject())
                ]
                csvwriter.writerow(row)
                
                if is_failing_grade(row[3]):
                    failing_grade_row = row  # Save the first failing grade row
                    has_failing_grade = True

                if has_failing_grade:
                    # Create one more row for the same student ID
                    row = [
                        student_id,
                        # Term
                        str(int(failing_grade_row[1]) + 10),
                        # Session
                        failing_grade_row[2],
                        # Grade
                        grade_gen(),
                        # Subject
                        failing_grade_row[4],
                    ]
                    csvwriter.writerow(row)
                    has_failing_grade = False


output_filename = 'student_records.csv'

create_and_write_to_csv(output_filename)

print(f"Data has been written to {output_filename}! Good Job {user}!")