let jRizz = {
  hourlyPayRate : 20,
  hoursWorkedPerWeek : 40,
  //  overTime : 40 + ((hoursWorkedPerWeek - 40) * 1.5),
  payFrequency : 52 / 26,
  grossIncome : this.hoursWorkedPerWeek * this.hourlyPayRate * this.payFrequency,
  grossYearlyIncome : this.hoursWorkedPerWeek * this.hourlyPayRate * 52,

  medicalPerMonth : 365.75,
  visionPerMonth : 27.6,
  dentalPerMonth : 118.85,
  monthlyBenefitsExpense : this.medicalPerMonth + this.visionPerMonth + this.dentalPerMonth,
  paycheckDeduction : this.monthlyBenefitsExpense / this.payFrequency,

  stateTaxWithholding : 0.036,
  // fed
  socialSecurityWithholding : .062,
  medicareWithholding : .0145,

  electricity : 100,
  water : 45,
  trash : 15,
  gas : 25,
  phones : 120,
  rent : 840,
  internet : 80,
  netflix : 12,
  braces : 0,
  hospital : 0,
  spotify : 0,
  fuel : 80,
  xbox : 0,
  insurance : 223,
  malibu : 334,
  diapers : 100,
};

let p = document.creatElement("p");
let newNode = document.createTextNode(jRizz.electricity);
p.appendChild(node);
let div = document.getElementById("demo");
div.appendChild(p);
// console.log(jRizz.electricity);
