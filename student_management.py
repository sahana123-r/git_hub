# Student Management Program

print("STUDENT MANAGEMENT SYSTEM")

name = input("Enter student name: ")
usn = input("Enter student USN: ")

# Enter marks
m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("\n--- Student Details ---")
print("Name:", name)
print("USN:", usn)
print("Subject 1 Marks:", m1)
print("Subject 2 Marks:", m2)
print("Subject 3 Marks:", m3)
print("Total Marks:", total)
print("Average Marks:", average)
print("good job")
