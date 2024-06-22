'''Project 2:Get 5 student names and for each student get 5 subjects marks .Display the student name and total marks.'''
for i in range(5):
    name=input("Enter the students name")
    total=0
    for i in range(5):
        marks=int(input("Enter the marks"))
        total+=marks
    print("The total marks of" ,name, "is :" ,total, )

