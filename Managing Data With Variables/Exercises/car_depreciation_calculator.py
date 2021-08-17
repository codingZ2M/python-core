
# Car Depreciation Calculator
# Years & Depreciation rate
# 2021 = 0%
# 2020 = 19%
# 2019 = 24%
# 2018 = 33%

purchase_price = float(input("Car Purchase Price: "))
car_purchase_year = int(input("Year Of Car Purchase: "))

depreciation_rate = float(input("Car Depreciation Rate: "))

residual_value = 100.00 - depreciation_rate

depreciation_cost = purchase_price * (depreciation_rate / 100)
current_selling_price =  purchase_price - depreciation_cost

print(f"You can sell you car @ {current_selling_price}  Residual value: {residual_value}")