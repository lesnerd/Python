def gradingStudents(grades):
    for grade in grades:
        from_next_five = 5 - (grade % 5)
        rounded = grade + from_next_five
        if grade < 38:
            print(grade)
        elif rounded - grade < 3:
            print(rounded)
        else:
            print(grade)


gradingStudents([75, 67, 40, 33])
print("\n")
gradingStudents([4, 73, 67, 38, 33])