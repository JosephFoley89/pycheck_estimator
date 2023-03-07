from decimal import Decimal

sal = 0      #salary
inc = 0.03   #percentage increase over last year
tx  = 0.24   #tax percentage could map the values to ranges but eh
frq = 12     #payment frequency
ret = 0.06   #percentage to go to your retiremnet fund

# this function assumes a pre-tax retirement deduction 
def paycheck_estimate(salary, increase, tax, ret, frequency):
    increase = salary * increase
    salary   = salary + increase
    retire   = salary * ret
    taxes    = salary * tax
    takehome = ((salary - ret) - taxes) / frq
    
    increase = Decimal(increase).quantize(Decimal('1.00'))
    salary   = Decimal(salary).quantize(Decimal('1.00'))
    retire   = Decimal(retire).quantize(Decimal('1.00'))
    taxes    = Decimal(taxes).quantize(Decimal('1.00'))
    takehome = Decimal(takehome).quantize(Decimal('1.00'))
    
    print (
        f'Your salary will increase ${increase} annualy.\n' +
        f'Which makes your annual salary ${salary}\n' + 
        f'You will put ${retire} into retirement this year.\n' +
        f'You will pay ${taxes} in taxes next year.\n' +
        f'You\'ll bring home ${takehome} per month.\n' +
        '\n--------------------------------------------\n'
    )
    
#running the gamut of potential increases to the tenth of a percentage point 
while (inc < 0.07):
    paycheck_estimate(sal, inc, tx, ret, frq)
    inc += .001