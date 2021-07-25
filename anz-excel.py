
import sys

cardfile = sys.argv[1]

csv_name=cardfile + ".csv"
lines = None
with open(cardfile) as cf:
    lines = cf.readlines()

expense = ""
for line in lines:
    line = line.strip() 
    #print(">" + line + ">")
    if ( "More Info Press to show" in line ):
        print(expense)
        expense = ""
    elif( line and not ("6671" in line) ):
        if ("$" in line):
            money = line[1:]
            expense = expense + money
        else:
            expense = expense + line + ", "

print(expense)
