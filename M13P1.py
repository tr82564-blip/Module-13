# input section

student_grades = {
    "Juan": 92,
    "Ana": 85,
    "Luis": 78
}

# processing section

total_grades = sum(student_grades.values())
class_average = total_grades / len(student_grades)

# output section

print(f"{'Student Name':<18}{'Grade':>8}")

for student_name, student_grade in student_grades.items():
    print(f"{student_name:<18}{student_grade:>8.2f}")

print(f"{'Class Average':<18}{class_average:>8.2f}")