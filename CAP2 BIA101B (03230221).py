class Employee:
    """
    Represents an employee with income and deductions.
    """

    def __init__(self, name, income):
        """
        Initializes an Employee object with name, income, and empty deductions.
        """
        self.name = name
        self.income = income
        self.deductions = {'NPPF': 0, 'GIS': 0}

    def calculate_tax(self):
        """
        Calculates the tax based on the employee's income and deductions.
        Returns the total tax amount.
        """
        self.calculate_deductions()
        taxable_income = self.income - sum(self.deductions.values())
        tax_rate = self.get_tax_rate(taxable_income)
        tax = self.apply_tax(tax_rate, taxable_income)
        return tax

    def calculate_deductions(self):
        """
        Calculates and sets the deductions for the employee.
        """
        self.deductions['Education Allowance'] = min(350000, self.income * 0.1)
        self.deductions['Other'] = self.income * 0.05

    def get_tax_rate(self, taxable_income):
        """
        Determines the tax rate based on taxable income brackets.
        """
        if taxable_income <= 300000:
            return 0
        elif taxable_income <= 400000:
            return 0.1
        elif taxable_income <= 650000:
            return 0.15
        elif taxable_income <= 1000000:
            return 0.2
        elif taxable_income <= 1500000:
            return 0.25
        else:
            return 0.3

    def apply_tax(self, rate, taxable_income):
        """
        Applies the tax rate to the taxable income.
        """
        if rate == 0:
            return 0
        elif rate == 0.1:
            return (taxable_income - 300000) * rate
        elif rate == 0.15:
            return (taxable_income - 400000) * rate + 10000
        elif rate == 0.2:
            return (taxable_income - 650000) * rate + 35000
        elif rate == 0.25:
            return (taxable_income - 1000000) * rate + 75000
        else:
            return (taxable_income - 1500000) * rate + 125000

    def __str__(self):
        """
        Returns a string representation of the Employee object.
        """
        return f"Employee: {self.name}, Income: Nu{self.income:,.2f}, Tax: Nu{self.calculate_tax():,.2f}"


class GovernmentEmployee(Employee):
    """
    Represents a government employee with specific deduction calculations.
    """

    def __init__(self, name, income):
        super().__init__(name, income)
        self.employee_type = 'Government'

    def calculate_deductions(self):
        """
        Overrides the calculate_deductions method for Government Employees.
        """
        super().calculate_deductions()
        self.deductions['NPPF'] = self.income * 0.1
        self.deductions['GIS'] = self.income * 0.05


class PrivateEmployee(Employee):
    """
    Represents a private employee with specific deduction calculations.
    """

    def __init__(self, name, income):
        super().__init__(name, income)
        self.employee_type = 'Private'

    def calculate_deductions(self):
        """
        Overrides the calculate_deductions method for Private Employees.
        """
        super().calculate_deductions()
        self.deductions['NPPF'] = self.income * 0.05
        self.deductions['GIS'] = self.income * 0.02


class ContractEmployee(Employee):
    """
    Represents a contract employee with specific deduction input.
    """

    def __init__(self, name, income):
        super().__init__(name, income)
        self.employee_type = 'Contract'

    def calculate_deductions(self):
        """
        Overrides the calculate_deductions method for Contract Employees.
        """
        super().calculate_deductions()
        self.deductions['GIS'] = float(input("Enter GIS deduction for contract employee: "))


def get_valid_income():
    """
    Validates and returns a positive floating-point income value.
    """
    while True:
        income_input = input("Enter employee income: Nu")
        try:
            income = float(income_input)
            if income < 0:
                print("Income cannot be negative. Please enter a valid income.")
            else:
                return income
        except ValueError:
            print("Invalid input. Please enter a valid number for income.")


def get_valid_employee_type():
    """
    Validates and returns a valid employee type ('government', 'private', 'contract').
    """
    while True:
        employee_type = input("Enter employee type (Government/Private/Contract): ").lower()
        if employee_type in ['government', 'private', 'contract']:
            return employee_type
        else:
            print("Invalid employee type. Please enter Government, Private, or Contract.")


# Main Program Execution
print("Welcome to the Employee Tax Calculator!")
name = input("Enter employee name: ")
income = get_valid_income()
employee_type = get_valid_employee_type()

if employee_type == 'government':
    employee = GovernmentEmployee(name, income)
elif employee_type == 'private':
    employee = PrivateEmployee(name, income)
elif employee_type == 'contract':
    employee = ContractEmployee(name, income)

print("\nTax Calculation Summary:")
print(employee)
