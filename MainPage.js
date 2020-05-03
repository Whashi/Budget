let hourlyPayRate = 20;
let hoursWorkedPerWeek = 40;
// let overTime = 40 + ((hoursWorkedPerWeek - 40) * 1.5);
let payFrequency = 52 / 26;
let grossIncome = hoursWorkedPerWeek * hourlyPayRate * payFrequency;
let grossYearlyIncome = hoursWorkedPerWeek * hourlyPayRate * 52;

let medicalPerMonth = 365.75;
let visionPerMonth = 27.6;
let dentalPerMonth = 118.85;
let monthlyBenefitsExpense = medicalPerMonth + visionPerMonth + dentalPerMonth;
let paycheckDeduction = monthlyBenefitsExpense / payFrequency;

let stateTaxWithholding = 0.036;
// fed
let socialSecurityWithholding = .062;
let medicareWithholding = .0145;
