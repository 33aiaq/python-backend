def tip_calculator():
    print("Welcome to the Tip Calculator!")

    bill = float(input("What was the total bill? $"))
    tip_percent = int(input("What the tip would you like to give? "))
    people = int(input("How many employees? "))

    tip_amount = bill * (tip_percent / 100)
    total_bill = bill + tip_amount
    per_person = total_bill / people

    print(f"Each employee should pay: ${per_person:.2f}")

tip_calculator()
