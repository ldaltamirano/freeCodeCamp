class Category:
    def __init__(self, category):
       self.category = category
       self.ledger = []
       self.totalDeposit = 0
       self.totalWithdraw = 0
    
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': float(amount), 'description': description })
        self.totalDeposit += float(amount)
    
    def withdraw(self, amount, description = ""):
        if(self.check_funds(amount) == False):
            return False
        self.ledger.append({'amount': float(-amount), 'description': description })
        self.totalWithdraw += float(amount)
        return True
    
    def check_funds (self, amount):
        return amount <= self.totalDeposit - self.totalWithdraw

    def transfer(self, amount,category):
        
        if(not self.check_funds(amount)):
            return False
        
        self.withdraw(float(amount), "Transfer to " + category.category)
        category.deposit(float(amount), "Transfer from " + self.category)

        return True

    def get_balance(self):
        return self.totalDeposit - self.totalWithdraw     
    
    def __str__(self):
        chars = 30
        countChars = len(self.category)
        count = (chars - countChars) / 2
        ast = "*" * int(count)
        titleLine = ast + self.category + ast + '\n'
        total = 0
        for ld in self.ledger:
            if(len(ld["description"])) > chars - len(str("%.2f" % ld["amount"])):
                count = 1
                space = " " * int(count)
                titleLine += ld["description"][0:chars - len(str("%.2f" % ld["amount"]))-1] + space + str("%.2f" % ld["amount"]) + '\n'
            else:
                countChars = len(str(float("%.2f" % ld["amount"]))) + len(str(ld["description"])) + 1
                count = (chars - countChars)
                space = " " * int(count)
                titleLine += str(ld["description"][0:countChars-1]) + space + str("%.2f" % ld["amount"]) + '\n'
        titleLine += "Total: " + str(float(self.totalDeposit) - float(self.totalWithdraw)) 
        return titleLine

def roundBy(x, base=10):
    return int(base * round(float(x)/base))
     
def getMaxCateoryNameLen(wdPercent):  
    length = 0
    for percent in wdPercent:
        for pc in percent:
            if(type(pc) is str):
                if(len(pc) > length):
                    length = len(pc)
    return length

def create_spend_chart(categories):
    withDraw = []
    wdPercent = []
    totalWithdraw = 0
    printLine = "Percentage spent by category\n"
    for cat in categories:
        withDraw.append({cat.category: cat.totalWithdraw})
        totalWithdraw += cat.totalWithdraw

    for wd in withDraw:
        for cat in wd:
            if(wd[cat]*100/totalWithdraw > 10):
                value = roundBy(round(wd[cat]*100/totalWithdraw))
                wdPercent.append([cat, value])
            else: 
                wdPercent.append([cat, 0])
    index = 100
    while(index >= 0):
        if(index == 100):
            printLine += str(index) + "| "
        elif(index != 0):
            printLine += " "+str(index) + "| "
        else:
            printLine += "  "+str(index) + "| "

        for percent in wdPercent:
            if(percent[1] >= index):
                printLine += "o  "
            else:
                printLine += "   "
        printLine += '\n'
        index-=10   
    printLine += " "*4 + "-"*10 + '\n'
    
    length = getMaxCateoryNameLen(wdPercent)
    for i in range(length):
        printLine += "     "
        for percent in wdPercent:
            for pc in percent:
                if(type(pc) is str):
                    if(len(pc) > i):
                        printLine += pc[i]+"  "
                    else:
                        printLine += "   "
        if(i + 1 != length):
            printLine += '\n'
    return printLine

