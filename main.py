import federaltaxes

# income data
pay_rate = 20.0
hours_per_week = 80
hours_per_week = 80 + ((hours_per_week - 80) * 1.5)  # calculate overtime
paychecks_per_year = 26
biweekly_pay_rate = pay_rate * hours_per_week

# benefit dictionary
benefits = {"medical": 365.78, "vision": 27.60, "dental": 118.85}
benefit_total = sum(benefits.values())
biweekly_benefit_total = benefit_total / 2

# tax data
arizona = 0.036
federal = federaltaxes.calculate_withholding(biweekly_pay_rate, paychecks_per_year)
social_security = .062
medicare = .0145

# expenses dictionary
expenses = {"electricity": 100, "water": 45, "trash": 15, "gas": 25, "phones": 120, "rent": 0, "internet": 80,
            "netflix": 12, "braces": 0, "hospital": 0, "spotify": 0, "fuel": 80, "oil": 20, "food": 300, "youtube": 12,
            "xbox": 0, "insurance": 223, "malibu": 334, "diapers": 100}


az_wh = round(biweekly_pay_rate * arizona, 2)
ss_wh = round(biweekly_pay_rate * social_security, 2)
mc_wh = round(biweekly_pay_rate * medicare, 2)

take_home = biweekly_pay_rate - az_wh - ss_wh - mc_wh - federal - biweekly_benefit_total
monthly_take_home = take_home * 2


print(round(monthly_take_home, 2))
print(sum(expenses.values()))
print(round(monthly_take_home - sum(expenses.values()), 2))
