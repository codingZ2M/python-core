def plan_details(plan):
    plan.get_health_insurance_type()
    plan.get_plan_name()
    plan.get_key_takeaways()
    plan.get_plan_eligibility()
    plan.get_expense_covers()
    plan.get_plan_details()
    plan.get_sign_up()


medicare_plans = [
    {
        'eligibility': ['Age 65 or older',
                        'Get disability benefits from Social Security for at least 25 months',
                        'Get disability benefits because you have Amyotrophic Lateral Sclerosis (ALS)',
                        'Have end-stage renal disease (ESRD) and meet certain requirements'
                        ],
        'expenses_covers': ['Semi-private rooms at skilled nursing facilities',
                            'Inpatient care',
                            'Supplies',
                            'Drugs during a hospital stay',
                            'Physical and occupational therapy in your home if you are home-bound',
                            'Doctor’s services',
                            'Medication'
                            ],
        'key_takeaways': ['Pays for care at a hospital',
                          'Skilled nursing facility or nursing home'
                          ]
    },

    {
        'eligibility': ['Are age 65 or older',
                        'Are under age 65 and have a disability',
                        'Have End-Stage Renal Disease (ESRD)',
                        "Have Amyotrophic Lateral Sclerosis, also called Lou Gehrig's disease"
                        ],
        'expenses_covers': ['Pays a portion of non-hospital provided medical care',
                            'Doctor visits and other outpatient services',
                            'Preventive services',
                            'Ambulance services',
                            'Mental health costs',
                            'Durable medical equipment'
                            ],
        'key_takeaways': ['Medicare Part B covers ambulance services, doctor visits, lab results, and certain medical '
                          'equipment',
                          'In contrast to Part A, which is available to many people at no cost, Part B is paid for '
                          'with monthly premiums '
                          ]
    }

]
