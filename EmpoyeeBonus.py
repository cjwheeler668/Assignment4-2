"""
EmployeeBonus.py
"""
#Initialize variables here
BONUS_1 = 50.00 
BONUS_2 = 75.00
BONUS_3 = 100.00
BONUS_4 = 200.00

#Input employee name
employeeName = input("Enter employee's name: ") 
#Shifts
shiftString = input("Enter number of shifts: ")
#Transact
transactionString = input("Enter number of transactions: ")
#Dollar
dollarString = input("Enter transactions dollar value: ")

#Delcare
numShifts = float(shiftString)
numTransactions = float(transactionString)
dollarValue = float(dollarString)

#if statements
ProductivityScore = (dollarValue/numTransactions)/numShifts
if ProductivityScore >= 200.00:
    bonus = BONUS_4
elif ProductivityScore >= 70 and ProductivityScore <= 199:
    bonus = BONUS_3
elif ProductivityScore >+ 31 and ProductivityScore <= 69:
    bonus = BONUS_2
elif ProductivityScore <= 50:
    bonus = BONUS_1

#Output
print("Employee Name: " + employeeName)
print("Employee Bonus: $" + str(bonus))