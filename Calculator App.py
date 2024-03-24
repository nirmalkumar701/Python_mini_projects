class Calculator:
    def addittion(self,num1,num2):
        return num1+num2
    def substraction(self,num1,num2):
        return num1-num2
    def division(self,num1,num2):
        return num1/num2
    def multiplication(self,num1,num2):
        return num1*num2

cal=Calculator()

while True:
    print("1.Perform Addition")
    print("2.Perform substravtion")
    print("3.Perform Division")
    print("4.Perform Multiplication")
    print("5.Exit")
    choice=int(input("choice:"))
    if choice ==1:
        num1=int(input("num1:"))
        num2=int(input("num2:"))
        print(cal.addittion(num1,num2))
    if choice ==2:
        num1=int(input("num1:"))
        num2=int(input("num2:"))
        print(cal.substraction(num1,num2))
    if choice ==3:
        num1=int(input("num1:"))
        num2=int(input("num2:"))
        if num2 != 0:
            print(cal.division(num1,num2))
        else:
            print( "Can not divide by Zero3")
    if choice ==4:
        num1=int(input("num1:"))
        num2=int(input("num2:"))
        print(cal.multiplication(num1,num2))
    if choice ==5:
       break