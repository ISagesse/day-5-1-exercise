# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
totalHeight = 0

for height in student_heights:
  totalHeight += height

number_of_student = 0

for student in student_heights:
  number_of_student += 1

average_student = round(totalHeight / number_of_student)

print(f"The average student heights is {average_student}")