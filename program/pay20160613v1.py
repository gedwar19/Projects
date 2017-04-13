#Gilbert Edwards
'''
this will compute gross pay based on pay
rate and hours worked.
'''

#def main():
def determine_tax_rate(gross):
    #global names can be use to access veriable locate in elsewhere, but not recommended 
    if gross> 1000:
        rate = 0.15
    elif gross > 800:
        rate = 0.1
    else:
        rate =0.08
    return rate
class paycheckPrinter:

    def print_paycheck(self,name, gross, rate, net, taxes):
        print ("Your gross pay was $%.2f" %gross)
        print("Your tax rate was %.2f%%." % (tax_rate *100))
        print ("You owe $%.2f in taxes" %taxes)
        print ("Your net pay was $%.2f" %net)
    
names = [Ray, Mary, Pat]
for n in names:
    print("Employee %s" % names)
    
do_again = "y"

while do_again == "y":
    do_again = input("Another employee (y or n)? ")
    do_again = do_again.lower().strip()
emp_count = int (input ("How many employee do you have?"))
for i in range (emp_count):
name = input('Enter your name: ')
pay_rate = float(input ("what is your hourly pay rate? "))
hours_worked = float(input ("How many hours did you work? "))
gross = pay_rate * hours_worked

tax_rate = determine_tax_rate(gross)
    
taxes =  tax_rate * gross
net = gross - taxes
printer = Paycheck_Printer()  
printer.print_paycheck(name, gross, tax_rate, net, taxes)

'''
if _name_=="_main_"
    main()
'''
