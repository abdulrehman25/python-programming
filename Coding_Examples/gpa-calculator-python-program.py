total_subjects = int(input("Enter No of Subjects ?:"))
i = 1
# array for storing multiple subjects
subjects = []

# getting user input for the subjects
while i <= total_subjects:
    # dictionary for subject
    subject = {}
    subject["name"] = input("Enter {} Subject Name:".format(i))
    subject["total_marks"] = int(input("Enter {} Subject Total Marks:".format(i)))
    subject["obtained_marks"] = float(input("Enter {} Subject Obtained Marks:".format(i)))
    subject["credit_hours"] = float(input("Enter {} Subject Credit Hours:".format(i)))
    subjects.append(subject)
    i = i + 1

print("============================================")
print("===============Subjects Details=============")
# printing all the subjects details
for subject in subjects:
    print(subject)
    print()
# calculating subject GPA


def calculate(obtained_marks):
    if obtained_marks >= 80:
        return 4
    elif obtained_marks >= 70 and obtained_marks < 80:
        return 3
    elif obtained_marks >= 60 and obtained_marks < 70:
        return 2
    elif obtained_marks >= 50 and obtained_marks < 60:
        return 1
    elif obtained_marks < 50:
        return 0


for subject in subjects:
    subject["subject_gpa"] = calculate(subject["obtained_marks"])
# printing all the subjects details with every subject gpa
print()
print()
print()
for subject in subjects:
    print(subject)
    print()


for subject in subjects:
    subject["quality_points"] = subject["credit_hours"] * subject["subject_gpa"]
total_gpa = 0.0
total_quality_points = 0
total_credit_hours = 0
for subject in subjects:
    total_quality_points = total_quality_points + subject["quality_points"]
    total_credit_hours = total_credit_hours + subject["credit_hours"]
    total_gpa = total_quality_points / total_credit_hours

for subject in subjects:
    print(subject)
    print()
print("================================")
print("Total GPA of Semester is {}:".format(total_gpa))