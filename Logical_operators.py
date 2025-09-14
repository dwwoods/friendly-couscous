#and operator both conditions are true
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
  print("Eligable for Loan")

#or operator

has_high_income2 = True
has_good_credit2 = False

if has_high_income2 or has_good_credit2:
  print("Eligable for Loan")

#not reverses the boolian
has_high_income3 = True
has_criminal_record = False
if has_high_income3 and not has_criminal_record:
    print("Eligable for Loan")
