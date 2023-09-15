from decimal import Decimal
from range_key_dict import RangeKeyDict

#2023 tax brackets
taxbracket = RangeKeyDict({
    (0,11000)            : .10,
    (11001,44725)        : .12,
    (44726,95375)        : .22,
    (95376,182100)       : .24,
    (182101,231250)      : .32,
    (231251,578125)      : .35,
    (578126,99999999999) : .37 
})

sal = 100000            #salary
inc = 0.03              #percentage increase over last year
txr = taxbracket[sal]   #tax percentage
frq = 12                #payment frequency
ret = 0.06              #percentage to go to your retiremnet fund

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
