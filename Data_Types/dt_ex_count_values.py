# Instructions
# Like the previous exercise, find the proper function or method that counts how many 10.0
# items there are in student_grades list and print out the output using a print() function.

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
#print(student_grades.count(10.0)) # His answer

# Over thinking it...a bit
count = 0
for grade in student_grades:
    if grade == 10.0:
        count = count + 1 
    else:
        continue
if count > 0:
    print('Number of students with a 10.0:', count)
else:
    print('These students are stupid...')
