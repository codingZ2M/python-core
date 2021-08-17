from insurance.medicare.Plan import Plan

# Inheritance
class MedicarePlanD(Plan):
    def __init__(self, health_insurance_type, plan_name, eligibility, expenses_covers, key_takeaways,
                 sign_up, plan_details):
        super().__init__(health_insurance_type, plan_name, eligibility, expenses_covers, key_takeaways)
        self.sign_up = sign_up
        self.plan_details = plan_details

        # Method Overriding - Runtime Polymorphism
    def get_plan_details(self):
        print(f'Plan Details {self.plan_name}')

        # Method Overriding - Runtime Polymorphism
    def get_sign_up(self):
        print(f'Signed up in {self.plan_name}')
