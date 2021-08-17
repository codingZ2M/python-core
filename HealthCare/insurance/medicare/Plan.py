# Abstraction
class Plan(object):
    def __init__(self, health_insurance_type, plan_name, eligibility, expenses_covers, key_takeaways ):
        self.health_insurance_type = health_insurance_type
        self.plan_name = plan_name
        self.eligibility = eligibility
        self.expenses_covers = expenses_covers
        self.key_takeaways = key_takeaways

    def get_key_takeaways(self):
        print('************** Key Takeaways *************************')
        for takeaway in self.key_takeaways:
            print(takeaway)
        print()

    def get_plan_eligibility(self):
        print('************** Plan Eligibility *************************')
        for eligibility in self.eligibility:
            print(eligibility)
        print()

    def get_expense_covers(self):
        print('************** Expenses Covers *************************')
        for expense in self.expenses_covers:
            print(expense)
        print()

    def get_health_insurance_type(self):
        print(f'Health Insurance Type: {self.health_insurance_type}')

    def get_plan_name(self):
        print(f'Plan Name: {self.plan_name}')
        print()

    def get_plan_details(self):
        print('To Be Overridden')

    def get_sign_up(self):
        print('To Be Overridden')


