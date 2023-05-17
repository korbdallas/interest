#A = P(1 + (r/n)/100)nt
#
#where:
#
#    A: Final Amount
#    P: Initial Principal
#    r: Annual Interest Rate
#    n: Number of compounding periods per year
#    t: Number of years

import math
import locale

locale.setlocale( locale.LC_ALL, '' )
   # gather needed data 
principle=int(input("Enter starting principle: \t"))
annual_rate=float(input("Enter annual interest rate: \t"))
num_compounds=int(input("Enter number of compounds per year: \t"))
num_years=int(input("Enter number of years to invest: \t"))

amount=float(principle*(pow((1 + (annual_rate/num_compounds)/100), num_compounds * num_years)))
interest_earned=float(amount-principle)
 
print("In", int(num_years), "years your investment will be worth", locale.currency(amount, grouping=True))
print("You would earn", locale.currency(interest_earned, grouping=True), "in", num_years, "years")
