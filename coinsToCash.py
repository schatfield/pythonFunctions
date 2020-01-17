import math 


"""Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.

quarters
nickels
dimes
pennies
For each coin type, give yourself as many as you like.

piggyBank = {
    "pennies": 342,
    "nickels": 9,
    "dimes": 32
}"""


def calc_dollars():
    piggyBank = {
    "pennies": 342,
    "nickels": 9,
    "dimes": 32,
    "quarters": 100
}

    pennies_value = piggyBank["pennies"] * .01
    nickels_value = piggyBank["nickels"] * .05
    dimes_value = piggyBank["dimes"] *.10
    quarters_value = piggyBank["quarters"] * .25

    dollar_amount = pennies_value + nickels_value + dimes_value + quarters_value

    print(dollar_amount)

calc_dollars()

"""Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.
Given the coins shown above, the output would be 7.07 when you call calc_dollars()"""