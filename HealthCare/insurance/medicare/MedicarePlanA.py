from insurance.medicare.Plan import Plan

# Inheritance
class MedicarePlanA(Plan):

    def __init__(self, health_insurance_type, plan_name, eligibility, expenses_covers, key_takeaways,
                 sign_up, plan_details):
        super().__init__(health_insurance_type, plan_name, eligibility, expenses_covers, key_takeaways)
        self.sign_up = sign_up
        self.plan_details = plan_details

        # Method Overriding - Runtime Polymorphism
    def get_plan_details(self):
        print('******************** Plan Details *************************')
        with open(self.plan_details, mode='r') as planA_details_file:
            print(planA_details_file.read())
            print()

        # Method Overriding - Runtime Polymorphism
    def get_sign_up(self):
        print('******************** Signup Details *************************')
        with open(self.sign_up, mode='r') as planA_signup_file:
            print(planA_signup_file.read())

