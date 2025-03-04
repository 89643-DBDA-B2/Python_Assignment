student_details= [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
{'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
{'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]

updated_lst = []

for student in student_details :
    val1 = student['V'] 
    val2 = student['VI']
    average = (val1 + val2)/2
    student.pop('V')
    student.pop('VI')
    student['V+VI'] = average
    updated_lst.append(student)

print(f"The updated list of dictionary is {updated_lst}")