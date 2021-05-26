

print("Welcome to the tip calculator!")

bill = input("What was the total bill? ")


tip = input("How much tip would you like to give? 10, 12, or 15? ")

tip_2 = float(tip) / 100
tip_3 = float(bill) * float(tip_2)
tip_4 = float(bill) + float(tip_3)

people = input("How many people to split the bill? ")

each = round(tip_4, 2) / int(people)

print(f"Each person should pay: {each}")