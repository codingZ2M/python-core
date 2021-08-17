# Control Flow with nested if / else with Conditional Operators

  # Car Depreciation Calculator
  # Years & Depreciation rate
  # 2021 = 0%
  # 2020 = 19%
  # 2019 = 24%
  # 2018 = 33%

purchase_price = float(input("Car Purchase Price: "))

car_purchase_year = int(input("Year Of Car Purchase: "))
if car_purchase_year == 2021:
  depreciation_rate = 0.00
elif car_purchase_year == 2020:
  depreciation_rate = 19.00
elif car_purchase_year == 2019:
  depreciation_rate = 24.00
else:
  depreciation_rate = 33.00

residual_value = 100.00 - depreciation_rate


liability_coverage = bool(input("If your car has Liability Coverage ?, Enter 'yes', otherwise press 'Enter' key"))


if liability_coverage:   # Boolean variable in the conditions
  comprehensive_insurance = bool(
      input("If your car has Comprehensive Insurance ?, Enter 'yes', otherwise press 'Enter' key"))

  depreciation_cost = purchase_price * (depreciation_rate / 100)
  current_selling_price = purchase_price - depreciation_cost

  if comprehensive_insurance:
    print(f"You can sell you car @ {current_selling_price + 2000.00} | Residual value: {residual_value}")
  else:
    print(f"You can sell you car @ {current_selling_price} | Residual value: {residual_value}")
else:
  print("Kindly Check Your Car Insurance")