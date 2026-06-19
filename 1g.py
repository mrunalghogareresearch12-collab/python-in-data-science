students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Emma": 95
}

print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)
print("\nClass Average =", average)

top_student = max(students, key=students.get)
print("Highest Marks Student =", top_student)
print("Marks =", students[top_student])
