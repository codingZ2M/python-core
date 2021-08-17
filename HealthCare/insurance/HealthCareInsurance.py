from insurance.medicare.Plan import Plan
from insurance.medicare.MedicarePlanA import MedicarePlanA
from insurance.medicare.MedicarePlanB import MedicarePlanB
from insurance.medicare.MedicarePlanC import MedicarePlanC
from insurance.medicare.MedicarePlanD import MedicarePlanD

from insurance import Utility


class HealthCareInsurance():

    def medicare_plan(self, plan):
        Utility.plan_details(plan)


medicare_planA = MedicarePlanA('Medicare', 'MedicarePlanA',
                               Utility.medicare_plans[0]['eligibility'],
                               Utility.medicare_plans[0]['expenses_covers'],
                               Utility.medicare_plans[0]['key_takeaways'],
                               'medicare/scripts/signup_planA.txt',
                               'medicare/scripts/planA_details.txt')


medicare_planB = MedicarePlanB('Medicare', 'MedicarePlanB',
                               Utility.medicare_plans[1]['eligibility'],
                               Utility.medicare_plans[1]['expenses_covers'],
                               Utility.medicare_plans[1]['key_takeaways'],
                               'medicare/scripts/signup_planB.txt',
                               'medicare/scripts/planB_details.txt')

plans_list = ['Medicare PlanA', 'Medicare PlanB', 'Medicare PlanC', 'Medicare PlanD']
while True:
    medicare_plan_name = input('Enter Medicare Plan Name:')
    if medicare_plan_name == '':
        print('Enter Plan Name...')
    elif not medicare_plan_name in plans_list:
        print('Select one of these Medicare Plans...' + medicare_plan_name + ' is not available' )
        for plan in plans_list:
            print(f'Plan Name: {plan}')
    else:
        break

health_care_insurance = HealthCareInsurance()

if medicare_plan_name == 'Medicare PlanA':
    health_care_insurance.medicare_plan(medicare_planA)

elif medicare_plan_name == 'Medicare PlanB':
    health_care_insurance.medicare_plan(medicare_planB)
