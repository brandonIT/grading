def printDirections():
    print("Welcome to the Grading Machine!\nThis program is designed to convert your grades (in numbers)\nto their letter version counter parts.\nThe program will continue to read in grades until you enter -1.")

def getInt():
    num=0
    print("Please enter the numerical value of the grade")
    num=int(input())
    return num

def grading():
    grade = 0
    gradeCount = 0
    gradeSum = 0
    gradeAverage = 0.0
    gradeValue = 'A'
    printDirections()
    grade=getInt()
    if(grade==-1):
        print("You didn't enter any grades, please close the program and try again")
        return
    while(grade != -1):
        if((grade <= 100) and (grade >= 90)):
            gradeCount+=1
            gradeSum += grade
            print("The grade you entered is an A!")
        elif((grade < 90) and (grade >= 80)):
            gradeCount+=1
            gradeSum += grade
            print("The grade you entered is a B!")
        elif((grade < 80) and (grade >= 70)):
            gradeCount+=1
            gradeSum += grade
            print("The grade you entered is a C.")
        elif((grade < 70) and (grade >= 60)):
            gradeCount+=1
            gradeSum += grade
            print("The grade you entered is a D.")
        elif((grade < 70) and (grade >= 1)):
            gradeCount+=1
            gradeSum+=grade
            print("The grade you entered is an F.")
        else:
            print("You have entered an invalid grade, please try again")
            grade=getInt()
        grade=getInt()
    gradeAverage = gradeSum/gradeCount
    if((gradeAverage <= 100) and (gradeAverage >= 90)):
        gradeValue = 'A'
    elif((gradeAverage < 90) and (gradeAverage >= 80)):
         gradeValue = 'B'
    elif((gradeAverage < 80) and (gradeAverage >= 70)):
            gradeValue = 'C'
    elif((gradeAverage < 70) and (gradeAverage >= 60)):
            gradeValue = 'D'
    elif((gradeAverage < 60) and (gradeAverage >= 1)):
            gradeValue = 'F'
    else:
        print("Error in average ifs.")
    print("The average of the grades you entered (in numerical form) is {}.".format(gradeAverage))
    if((gradeValue == 'A') or (gradeValue == 'F')):
        print("The letter grade equivalent to {} is an {}.".format(gradeAverage,gradeValue))
    else:
        print("The letter grade equivalent to {} is a {}.".format(gradeAverage,gradeValue))

grading()
