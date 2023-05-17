#A = P(1 + (r/n)/100)nt
#
#where:
#
#    A: Final Amount
#    P: Initial Principal
#    r: Annual Interest Rate
#    n: Number of compounding periods per year
#    t: Number of years

import sys
import math
import locale

locale.setlocale( locale.LC_ALL, '' )


  # gather needed data 

def gather_principle():
    global principle
    principle=input("Enter starting principle: \t")
    try:  # checks if input is numeric
       principle = float(principle)
    except:
       print("Please enter values greater than 0. ")
       pass
       gather_principle()
    if principle < 1:
       print("Please enter values greater than 0. ")
       gather_principle()
    else:
       pass

def gather_annual_rate():
    global annual_rate
    annual_rate=(input("Enter annual interest rate: \t"))
    try:  # checks if input is numeric
       annual_rate = float(annual_rate)
    except:
       print("Please enter values greater than 0. ")
       pass
       gather_annual_rate()
    if annual_rate < 1:
       print("Please enter values greater than 0. ")
       gather_annual_rate()
    else:
       pass 
    
def gather_num_compounds():
    global num_compounds
    num_compounds=(input("Enter number of compounds per year: \t"))
    try:  # checks if input is numeric
       num_compounds = float(num_compounds)
    except:
       print("Please enter values greater than 0. ")
       pass
       gather_num_compounds()
    if num_compounds < 1:
       print("Please enter values greater than 0. ")
       gather_num_compounds()
    else:
       pass

def gather_num_years():
    global num_years
    num_years=(input("Enter number of years to invest: \t"))
    try:  # checks if input is numeric
       num_years = float(num_years)
    except:
       print("Please enter values greater than 0. ")
       pass
       gather_num_years()
    if num_years < 1:
       print("Please enter values greater than 0. ")
       gather_num_years()
    else:
       pass


gather_principle()
gather_annual_rate()
gather_num_compounds()
gather_num_years()    

amount=(principle*(pow((1 + (annual_rate/num_compounds)/100), num_compounds * num_years)))
interest_earned=(amount-principle)

print("\nIn", int(num_years), "years your investment will be worth", locale.currency(amount, grouping=True))
print("You would earn", locale.currency(interest_earned, grouping=True), "in", int(num_years), "years")


