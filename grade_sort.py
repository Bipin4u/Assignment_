'''Given the names and grades for each
and print the name(s) of any student(s)
Note: If there are multiple students with the same grade, order their names alphabetically and print each
name on a new line.
Input Format
The first line contains an integer, 
The subsequent lines describe
the second line contains their grade.
Constraints
There will always be one or more
Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple
students, order their names alphabetically
'''
while(True):
    try:
        no_of_student=int(input("Enter the number of student: "))
        break
    except:
        print("Please give a integer value")

        continue

student_score=[]
dummy_score=list()
for _ in range(no_of_student):
    print()
    name = input("Enter the name of the student: ")
    while(True):
        try:
            score= float(input("Enter the score of the student: "))
            break
        except:
            print("please enter a numerical value")
            print("Re-enter the student details")
            continue
    student_score.append([name,score])

orderedlist = sorted(student_score, key=lambda x:x[0])
print()
print("The order of the student according to name is :")
[print(_) for _ in orderedlist]
orderedscore = sorted(student_score, key=lambda x:x[1])


list=[]

for _ in orderedscore:
    if _[1] in list:
        continue
    list.append(_[1])
try:
    second_least_number = list[1]
except:
    print("Every one has scored same grade")
    second_least_number=list[0]
print()
print("Second lowest grade student are: ")
for _ in orderedlist:
    if second_least_number in _:
        print(_)

