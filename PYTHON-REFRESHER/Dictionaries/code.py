# friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
# friends_ages["Adam"]
# print(friends_ages["Adam"])

# friends = [
#     {"name": "Rolf", "age": 24},
#     {"name": "Adam", "age":30},
#     {"name": "Anne", "age": 27}
# ]

# print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Adam": 80, "Anne": 100}

# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")
attendace_values =student_attendance.values()
print(sum(attendace_values)/len(attendace_values))