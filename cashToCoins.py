import math
# this is something called the "math module" and you need to google about it because it isn't a module in the sense you're thinking.

def make_change():
    dollar_amount = 8.69
    piggy_bank = {
        "pennies": 0,
        "nickles": 0,
        "dimes": 0 ,
        "quarters": 0
    }

    piggy_bank["quarters"] = math.floor(dollar_amount / .25)
    # what is math.floor? GOOGLE that

    dollar_amount = dollar_amount % .25
    piggy_bank["dimes"] = math.floor(dollar_amount / .10)

    piggy_bank["dimes"] = math.floor(dollar_amount / .05)

    dollar_amount = dollar_amount % .05
    piggy_bank["pennies"] = math.floor(dollar_amount / .01)

    return piggy_bank
print(make_change())

    # to find out if a number is even do % ?
    # % is called modulo
    # it also gives you what's left over
    # what is shortcut to copy lines


    #look up "while loops". Here's an example below:
    

#     def fill_piggy_bank (dollarAmount):
#     quarters_quantity = 0
#     dimes_quantity = 0
#     nickels_quantity = 0
#     pennies_quantity = 0
#     while dollarAmount > .25:
#         dollarAmount -= .25
#         quarters_quantity += 1
#     while dollarAmount > .1:
#         dollarAmount -= .1
#         dimes_quantity += 1
#     while dollarAmount > .05:
#         dollarAmount -= .05
#         nickels_quantity += 1
#     while dollarAmount > .01:
#         dollarAmount -= .01
#         pennies_quantity += 1
#     piggyBank.update({
#         'quarters': quarters_quantity,
#         'dimes': dimes_quantity,
#         'nickels': nickels_quantity,
#         'pennies': pennies_quantity
#     })
#     print(piggyBank)
# fill_piggy_bank(dollarAmount)