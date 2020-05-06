def calculate_withholding(weekly_gross, paycheck_frequency):
    # withholding tables
    bracket = 0
    withholding_brackets = [0, 11900, 31650, 92150, 182950, 338500, 426600, 633950]
    tentative_withholding = [0, 0, 1975, 9235, 29211, 66543, 94735, 167307.5]
    withholding_percentages = [0, .1, .12, .22, .24, .32, .35, .37]

    estimated_annual_gross_income = weekly_gross * paycheck_frequency
    adjusted_annual_gross = estimated_annual_gross_income - 12900  # later adjust here for 2 incomes

    # find tax bracket
    for i in range(8):
        bracket = i
        if estimated_annual_gross_income < withholding_brackets[i+1]:
            break

    # evaluate withholding
    withholding = adjusted_annual_gross - withholding_brackets[bracket]
    withholding = withholding * withholding_percentages[bracket]
    withholding = withholding + tentative_withholding[bracket]
    withholding = withholding / paycheck_frequency

    return round(withholding, 2)
