#case statement library for Python applications
#python has no inbuilt case/switch statement which is weird so heres one]


#this is a quick prototype version

def caseObj():
    case={}
    return case

def addCase(statement,caseName,caseAction):
    statement[caseName]=caseAction

def removeCase(statement,caseName):
    del statement[caseName]

def callCase(statement,case):
    return statement[case]

def returnCases(statement):
    print("caseName           caseAction")
    for x,y in statement:
        print(x+" "+y)
    return statement
