student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

# > Scores 91 - 100: Grade = "Outstanding"

# > Scores 81 - 90: Grade = "Exceeds Expectations"

# > Scores 71 - 80: Grade = "Acceptable"

# > Scores 70 or lower: Grade = "Fail"

# student_grades = {
#     "Outstanding":91,
#     "Exceeds Expectations":81,
#     "Acceptable":71,
#     "Fail":70
# }
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores :
    scores = student_scores[student]
    if scores >= 91:
        student_grades[student] = "Outstanding"
    elif scores >= 81 and scores < 91 :
        student_grades[student] = "Exceeds Expectations"
    elif scores >= 71 and scores < 81 :
        student_grades[student] = "Acceptable"
    elif scores < 71 :
        student_grades[student] = "Fail"

    

# 🚨 Don't change the code below 👇
print(student_grades)
