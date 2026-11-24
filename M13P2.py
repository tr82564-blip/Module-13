# function section

def calculate_class_averages(student_grades):
    class_averages = []

    for grade_index in range(3):
        total_grade = 0

        for grade_list in student_grades.values():
            total_grade = total_grade + grade_list[grade_index]

        class_average = total_grade / len(student_grades)
        class_averages.append(class_average)

    return class_averages


# input section

student_grades = {
    "Juan": [92, 88, 90],
    "Ana": [85, 90, 95],
    "Luis": [78, 82, 86]
}

# processing section

student_averages = {}

for student_name, grade_list in student_grades.items():
    student_averages[student_name] = sum(grade_list) / len(grade_list)

class_averages = calculate_class_averages(student_grades)

# output section

print(f"{'Student Name':<18}{'Average':>10}")

for student_name, student_average in student_averages.items():
    print(f"{student_name:<18}{student_average:>10.2f}")

print()
print(f"{'Assessment':<18}{'Class Average':>15}")

for grade_index in range(len(class_averages)):
    grade_label = f"Grade {grade_index + 1}"
    print(f"{grade_label:<18}{class_averages[grade_index]:>15.2f}")