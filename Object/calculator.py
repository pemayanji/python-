class Calculator:

    def  __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self,*args,**kwargs):
        self.num1 = args[0]
        print(self.num1)
        total = 0
        for n in args:
            total +=n
        return total
    

    def sub(self,*args):
        total = args[0]
        for i in args[1:]:
            total -=i
        return total
    
    def mul(self,*args):
        total = 1
        for i in args:
            total*=i
        return total
    
    def div(self,*args):
        try:
            total = args[0]
            for i in args[1:]:
                total/=i
            return total
        except ZeroDivisionError:
            print("Error: Division by Zero!")
    
cal=Calculator(1,2)
print(cal.num1)
print(cal.add(2,3,6))

print(cal.sub(10,2,5))
print(cal.mul(2,3,4,5))
print(cal.div(0,3))