# If applicant has high income AND good credit, eligible for loan
highIncome = True
goodCredit = True
criminalRecord = False

if highIncome and goodCredit:
    print("Eligible for loan")
else:
    print("Not Eligible")

# If applicant has high income OR good credit, eligible for loan:

if highIncome or goodCredit:
    print("Eligible for Loan")
else: 
    print("Not eligible")


#AND: both
#OR: one or the other
#NOT: Reverses a Boolean

if not criminalRecord:
    print(" No Criminal Record")

# Video Progess 1:11:04

