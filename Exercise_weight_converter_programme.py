Weight = int(input("Enter Weight: "))
units = input("(L)bs or (K)gs: ")
if units.upper() == "L":
    weight_kgs2 = Weight * 0.45
    print(f"You are {weight_kgs2} kilos")
else:
    weight_lbs2 = Weight / 0.45
    print(f"You are {weight_lbs2} pounds")