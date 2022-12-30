class Atm:
    def cbb(self):
        print("enter your name\n")
        name=input()
        name=name.capitalize()
        print("WELCOME",name)
        print("PLEASE ADD SOME FUNDS IN ACCOUNT PRESS 3 THEN CHECK")
        print("HAVE A NICE DAY VISIT AGAIN THANK YOU")
    def WM(self):
        print("enter your name\n")
        name=input()
        name=name.capitalize()
        print("WELCOME",name)
        print("ENTER AMOUT TO WITHDRAW\n")
        a=int(input())
        acc=int(input('''
        PRESS 1 FOR  SAVINGS 
        PRESS 2 FOR CURRENT
        '''))
        if acc==1 or acc==2:
            print("INFUCCIENT",a, " PLEASE ADD MONEY SAVE ACCOUNT")
            print("HAVE A NICE DAY VISIT AGAIN THANK YOU")
    def CM(self):
        print("enter your name\n")
        name=input()
        name=name.capitalize()
        print("WELCOME",name)
        print("ENTER AMOUT TO CREDIT\n")
        a=int(input())
        acc=int(input('''
        PRESS 1 FOR  SAVINGS 
        PRESS 2 FOR CURRENT
        '''))
        if acc==1 or acc==2:
            print(a," THIS AMOUT IS CREDITED TO YOUR ACCOUNT THANK YOU FOR USING US!!!")
            print("HAVE A NICE DAY VISIT AGAIN THANK YOU")
    def t(self):
        print("enter your name\n")
        name=input()
        name=name.capitalize()
        print("WELCOME",name)
        print("ENTER ACCOUNT NUMBER\n")
        a=int(input())
        print("NO TRANSACTION IN ",a)
        print("HAVE A NICE DAY VISIT AGAIN THANK YOU")   
        
        

while True:
    print("*****CREATED BY FATHERPRINCE*****")
    o=int(input('''
PRESS 1 FOR CHECK BANK BALANCE
PRESS 2 FOR WITHDRAW MONEY
PRESS 3 FOR CREDIT MONEY IN ACCOUNT
PRESS 4 FOR LAST 7 STAMENTS
PRESS 5 FOR EXIT\n'''))
    atm=Atm()
    if o==1:
        atm.cbb()
    elif o==2:
        atm.WM()    
    elif o==3:
       atm.CM()
    elif o==4:
        atm.t()
    else:
        break        
        
        
        
        
        
    
    
    
        
        