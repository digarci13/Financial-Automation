import csv
import calendar
import sys
import os

class financial_Automation:

    def readStatements(self):   
        transaction = []
        f = ''
        if len(sys.argv) == 2:
            f = sys.argv[1]
        path = os.getcwd()
        path = path +'\Bank_Statements\\' + f
        print(path)
        file_to_read = open(path , 'r') 
        csv_reader = csv.reader(file_to_read, delimiter='"')
        for line in csv_reader:
            t = line[0] + line[1]
            t = t.replace(",", " ")
            transaction.append(t)
        
        return transaction
    
    def CalMonthlyExpences(self):
        transactions = self.readStatements()
        total = 0
        month = 0
        expences = 0
        deposits = 0
        n = [] 
        for t in transactions:
            l = t.split()
            n = l[0].split("/")
            month = calendar.month_name[int(n[0])]
            if(float(l[1]) < 0):
                expences = round(expences + (float(l[1]) *-1), 2)
            else:
                deposits = round(deposits + float(l[1]), 2)
            total += float(l[1])
            total = round(total, 2)

        self.writeToFile(month, n[2], expences, deposits, total)

    def writeToFile(self, m, y, e, d, t):
        statementFile = open("file_statement.txt", "a") 
        #Date:
        #Total Expenses: 
        #Total Deposits:
        #Ending Balance:
        #Total Savings:
        #--------
        
        statementFile.write('Date: ' + m + " " + y +'\n')
        statementFile.write('Total Expenses: $' + str(e) + '\n')
        statementFile.write('Total Deposits: $' + str(d) + '\n')
        statementFile.write('Ending Balance: $' + str(t) + '\n')
        statementFile.write('Total Savings: $200 \n')
        statementFile.write('------------------------------------')
        statementFile.write('\n \n \n')




f = financial_Automation()
f.CalMonthlyExpences()
    

