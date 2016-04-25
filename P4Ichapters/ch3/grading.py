def header():
    # Print program title header
    print '\n'
    print '                   ##########################################                  '
    print '                   #                                        #                  '
    print '                   #       Py4Inf Progress Calculator       #                  '
    print '                   #========================================#                  '
    print '                   #        Written on July 19, 2014        #                  '
    print '                   #                                        #                  '    
    print '                   ##########################################                  '
    print '\n'

def divider():
    print '======================================================================'

def menu():
    # Prompt for input method
    mode = None
    print 'How do you want to input scores?'
    print '   1)Enter each assignment, quiz and extra credit score individually'
    print '   2)Enter the total for each type of evaluation'
    while mode is None:
        inp = raw_input("Select your mode (1-2): ")
        if inp == '1':
            print 'You selected to enter each score individually.\n'
            mode = 'list'
        elif inp == '2':
            print 'You selected to enter the total for each score.\n'
            mode = 'total'
        else:
            print 'Something went wrong. Please try again!\n'        
    return mode

def validate_inp(inp):
    # Validate input, map error/blank input to zero
    if inp.lower() == 'exit': exit()
    try:
        score = float(inp)
        return score
    except:
        print 'A zero has been assigned to your score.\n'
        return 0

def inputmsg(i, j=0, c=0, mode = ""):
    # Adapt prompt message to course material
    assignments = ['\'Hello World\'', '2.2', '2.3', '3.1', '3.3', '4.6', '5.2', '6.5', '7.1', '7.2', '8.4', '8.5', '9.4', '10.2']
    extracredit = ['Python Install Screen Shots', 'Essay 1', 'Essay 2', 'Essay 3']
    if mode == "total":
        standardmsg = "Enter the total {} score ('Exit' to quit): "
        inp = raw_input(standardmsg.format(i))
    else:
        standardmsg = "Enter the {} score ('Exit' to quit): "
        if i == 'Assignment':
            if j == 1:
                inp = raw_input(standardmsg.format(assignments[c] + " " + i))
            else:
                inp = raw_input(standardmsg.format(i + " " + assignments[c]))
        elif i == 'Extra Credit':
            inp = raw_input(standardmsg.format(extracredit[c]))
        elif i == 'Final Exam':            
            inp = raw_input(standardmsg.format(i))
        else:
            inp = raw_input("Enter the {}".format(i) + " {} score ('Exit' to quit): ".format(j))
    return inp

def score():
    # Calculate points for the course; total for the student, total possible
    mode = menu()
    coursetotal = 0
    coursepoints = 0
    coursework = {'Quiz': 10, 'Assignment': 14, 'Extra Credit': 4, 'Final Exam': 1}
    for i, val in coursework.items():
        if i == 'Final Exam':
            coursetotal += 20 * val
        elif i == 'Extra Credit':
            pass
        else:
            coursetotal += 10 * val

        c = -1
        if mode == 'total':
            points = validate_inp(inputmsg(i, 0, 0, "total"))
            coursepoints += points
        else:
            for j in range(1, val + 1):
                c += 1
                points = validate_inp(inputmsg(i, j, c))
                coursepoints += points
    return coursepoints, coursetotal

def scoresummary():
    # Print an ASCII report with user's progress
    myscore = score()
    coursepoints = myscore[0]
    coursetotal = myscore[1]
    divider()
    print ''
    print 'You have earned', float(coursepoints), 'points in this course, out of a possible', float(coursetotal), '({}%).'.format(round(coursepoints/coursetotal*100,2))
    if coursepoints > 40 + coursetotal:
        print 'Your score is out of range, even including all extra credit, and is likely incorrect.'
    elif coursepoints >= 0.9 * coursetotal:
        print 'Congratulations! You have earned enough points for a Statement / Certificate with Distinction.'
    elif coursepoints >= 0.75 * coursetotal:
        print 'Congratulations! You have earned enough points for a Statement of Accomplishment/Verified Certificate.'
    return coursepoints

def scale():
    # Grade scale diagram
    header()
    coursepoints = scoresummary()
    print ''
    print 'Milestone                               Score Range         Your Grade'
    print '----------------------------------------------------------------------'
    level1 = 'Participation                           0.00   - 194.99     '
    level2 = 'Statement of Accomplishment / Cert      195.00 - 233.99     '
    level3 = 'Statement / Cert with Distinction       234.00 - 259.99     '
    level4 = 'Perfect Score                           260.00 - 300.00     '
    arrow = '<='
    if coursepoints < 195: level1 += arrow
    elif 195 <= coursepoints < 234: level2 += arrow
    elif 234 <= coursepoints < 260: level3 += arrow
    elif 260 <= coursepoints <= 300: level4 += arrow
    elif coursepoints > 300:
        level1 += '?'
        level2 += '??'
        level3 += '???'
        level4 += '????'
    print level1
    print level2
    print level3
    print level4
    divider()
    print '\n'
    if coursepoints > 300:
        print 'Please try again!'

def main():
    scale()

if __name__ == '__main__':
    main()
