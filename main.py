print("Welcome to the tip calculator.")
totalBill= float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 12, 15, or 20? "))
split = float(input("How many people are splitting the bill? "))

tipPercent = 1 + (tip/100)
beforeTaxPP = totalBill/split

total = tipPercent * beforeTaxPP 
print(f"Each person should pay: ${round(total,2)}")
