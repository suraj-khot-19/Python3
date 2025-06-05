#!/bin/python3

'''
Reads the number of students and number of subjects.

Calculates the average for each student.

Assigns grades based on the average.

Returns the list of grades as per the rules you gave.

| Average    | Grade |
| ---------- | ----- |
| `>= 90`    | A+    |
| `[80, 90)` | A     |
| `[70, 80)` | B     |
| `[60, 70)` | C     |
| `[50, 60)` | D     |
| `< 50`     | F     |

'''

#
# Complete the 'calculateGrade' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_INTEGER_ARRAY students_marks as parameter.
#

def calculateGrade(students_marks):
    grades = []

    for marks in students_marks:
        avg = sum(marks) / len(marks)

        if avg >= 90:
            grades.append("A+")
        elif avg >= 80:
            grades.append("A")
        elif avg >= 70:
            grades.append("B")
        elif avg >= 60:
            grades.append("C")
        elif avg >= 50:
            grades.append("D")
        else:
            grades.append("F")

    return grades

if __name__ == '__main__':

    students_marks_rows = int(input().strip())
    students_marks_columns = int(input().strip())

    students_marks = []

    for _ in range(students_marks_rows):
        students_marks.append(list(map(int, input().rstrip().split())))

    result = calculateGrade(students_marks)
    print(result)
