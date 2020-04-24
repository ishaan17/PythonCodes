student=["Ram","rajat","rahul","ishaan"]
age=[23,24,54,12,12,56,78,90]
print(student)
student.append("rishabh")
for item in student:
    print(item)
student.insert(1,"harsh")
print(student)
for i in range(len(age)):
    print(age[i])
age.sort()
print(age)
age.reverse()
print(age)
age.count(12)
