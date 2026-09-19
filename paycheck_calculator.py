total_change_amount = int(input())
original_amount = total_change_amount

dollars = total_change_amount // 100
total_change_amount %= 100

quarters = total_change_amount // 25
total_change_amount %= 25

dimes = total_change_amount // 10
total_change_amount %= 10

nickels = total_change_amount // 5
total_change_amount %= 5

pennies = total_change_amount

if original_amount == 0:
    print("No change")
else:
    if dollars == 1:
        print(dollars, "Dollar")
    elif dollars > 1:
        print(dollars, "Dollars")

    if quarters == 1:
        print(quarters, "Quarter")
    elif quarters > 1:
        print(quarters, "Quarters")

    if dimes == 1:
        print(dimes, "Dime")
    elif dimes > 1:
        print(dimes, "Dimes")

    if nickels == 1:
        print(nickels, "Nickel")
    elif nickels > 1:
        print(nickels, "Nickels")

    if pennies == 1:
        print(pennies, "Penny")
    elif pennies > 1:
        print(pennies, "Pennies")
