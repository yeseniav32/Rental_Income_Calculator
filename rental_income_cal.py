from binascii import Incomplete


class Calculator(): #class that will be doing all the math behind every input

    def __init__(self):
        self.cost = None
        self.house_status = {
            "single": False,
        } 
        self.incomedict = {
            "completed": False,
        }
        self.income = None
        self.expensesdict = {
            "completed": False    
        }
        self.expenses = None
        self.cashflowdict = {
            "completed": False
        }
        self.cashflow = None
        self.roi = {}
        
    def input_check(self,text):
        while True:
            answer = input(text)
            if answer.isdigit():
                return int(answer)
            else:
                print("Please enter a numeric value only.")

    def cost_of_house(self):
        self.cost = self.input_check("How much does the property cost? ")

    def income_from_home(self):
        print("""
================
    INCOME
================
        """)
        rent_question = input("Do you plan on renting a multi-unit home or single house? Please only enter Single or Multi. ")
        if  rent_question.lower() == "single":
            self.house_status["single"] = True
            self.incomedict["rent"] = self.input_check("How much do you plan on renting the house? ")
        elif rent_question.lower() == "multi":
            self.incomedict["units"] = self.input_check("How many units do you plan to rent? ")
            self.incomedict["rent"] = self.input_check("How much do you plan to rent each unit for? ")
        else:
            print("Please enter only single or multi")
        other_income = input("Is there other income that will be coming from this house? Yes/No ")
        if other_income.lower() == "yes":
            self.incomedict["other income"] = self.input_check("How much additional income do you anticipate earning a month other than rent from this house? ")
        else:
            self.incomedict["other income"] = 0
        if rent_question.lower() == "single":
            self.income = self.incomedict.get("rent") + self.incomedict.get("other income") #total income for a single house rent
            print(f"The total income for your single rental income is {self.income}. ")
        else:
            self.income = self.incomedict.get("units") * self.incomedict.get("rent") + self.incomedict.get("other income") #total income for a multi-unit house rent
            print(f"The total income for your multi-unit rental is {self.income}. ")
        self.incomedict["completed"] = True
        print(self.incomedict)

    def expenses_of_home(self):
        print("""
================
    EXPENSES
================
        """)
        utilities = input("Will you be paying for your renters utilites? Yes / No ")
        if utilities.lower() == "yes":
            self.expensesdict["gas"] = self.input_check("How much do you anticipate the monthly gas bill to be? ")
            self.expensesdict["electricity"] = self.input_check("How much do you anticipate the monthly electricity bill to be? ")
            self.expensesdict["sewer"] = self.input_check("How much do you anticipate the monthly sewer bill to be? ")
            self.expensesdict["garbage"] = self.input_check("How much do you anticipate the monthly garbage bill to be? ")
            self.expensesdict["other"] = self.input_check("Are there other utitlies you expect to pay monthly? If so, how much? If you do not anticipate to pay other utilites, please enter 0. ")
            utilities_total = self.expensesdict.get("gas") + self.expensesdict.get("electricity") + self.expensesdict.get("sewer") + self.expensesdict.get("garbage") + self.expensesdict.get("other")
        else: 
            utilities_total = 0
        self.expensesdict["water"] = self.input_check("How much do you anticipate the monthly water bill to be? ")
        self.expensesdict["tax"] = self.input_check("What is the approximate amount of taxes you will be paying monthly? ")
        self.expensesdict["insurance"] = self.input_check("What is the approximate amount of insurance you will be paying monthly? ")
        self.expensesdict["hoa"] = self.input_check("How much do you expect to pay for HOA (Home Owner Association)? ")
        self.expensesdict["vacancy"] = self.input_check("How much do you plan to put aside monthly for when the house/apartment is vacant? ")
        self.expensesdict["repairs"] = self.input_check("How much do you plan to put aside monthly for unexpected repairs? ")
        self.expensesdict["capital exp"] = self.input_check("How much do you plan to put aside for capital expenditures? Example: roof, siding, plumbing, etc. ")
        self.expensesdict["property manager"] = self.input_check("How much do you plan to pay your property manager? If not aplicable, enter 0. ")
        self.expensesdict["mortgage"] = self.input_check("What is the approximate mortgage? ")
        self.expenses = utilities_total + self.expensesdict.get("water") + self.expensesdict.get("tax") + self.expensesdict.get("insurance") + self.expensesdict.get("hoa") + self.expensesdict.get("vacancy") + self.expensesdict.get("repairs") + self.expensesdict.get("capital exp") + self.expensesdict.get("property manager") + self.expensesdict.get("mortgage")
        print(f"Your total expenses for this property is {self.expenses}.")
        self.expensesdict["completed"] = True
        # print(self.expensesdict)

    def cash_flow(self):
        print("""
================
    CASH FLOW
================
        """)
        if self.incomedict["completed"] == False and self.expensesdict["completed"] == False:
            print("Please fill out the Income and Expense part of the form first in order to calculate your cash flow")
        elif self.incomedict["completed"] == False:
            print("Please ensure to fill out the Income part of the form to proceed with cash flow")
        elif self.expensesdict["completed"] == False:
            print("Please ensure to fill out the Expenses part of the form to proceed with cash flow")
        
        elif self.house_status["single"] == True:
            self.cashflow = self.income - self.expenses
            print(f"Your cash flow for a single home is {self.cashflow}")
            self.cashflowdict["completed"] = True
        elif self.house_status["single"] == False:
            self.cashflow = self.income - self.expenses
            print(f"Your cash flow for a multi-unit house is {self.cashflow}")
            self.cashflowdict["completed"] = True

    def return_on_investment(self):
        print("""
================
       ROI
================
        """)
        if self.cashflowdict["completed"] == False:
            print("Please ensure both Income and Expenses parts are filled out as the cash flow is needed to calculate ROI.")
        else: 
            self.roi["down payment"] = self.input_check("How much of a down payment will you be giving on this house? ")
            closing_cst = self.cost * 0.05
            self.roi["rehab repairs"] = self.input_check("How much do you plan to spend on repairs for this property after purchasing? ")
            self.roi["miscellaneous expenses"] = self.input_check("How much do you think you will spend in miscellaneous expenses? ")

            total_investment = self.roi.get("down payment") + closing_cst + self.roi.get("rehab repairs") + self.roi.get("miscellaneous expenses")
        
            if self.house_status["single"] == True:
                anual_cashflow = self.cashflow * 12
                roi = (anual_cashflow / total_investment) * 100
                print(f"Your ROI is {roi:.2%} with a cashflow of ${anual_cashflow} annually. ")
        
            elif self.house_status["single"] == False:
                anual_cashflow = self.cashflow * 12
                roi = (anual_cashflow / total_investment) * 100
                print(f"Your ROI is {roi:.2%} with a cashflow of ${anual_cashflow} annually. ")
            # print(self.roi)

    # def show_edit(self):
    #     for k,v in self.items():
    #             print(f"{k} - {v}")

    def edit(self):
        edit_option = self.input_check("""
 ================
       EDIT
================       

What section do you wish to edit?
    [1] INCOME
    [2] EXPENSES
    [3] ROI
    """)
        if edit_option == 1:
            for k,v in self.incomedict.items():
                print(f"{k} - {v}")
            edit_ask = input("""
Which part would you like to edit? 
For example if you would like to change the rent price please enter "rent". """)
            new_input = input("Please enter the value you wish to change it to ")
            self.incomedict[edit_ask] = new_input
        
        elif edit_option == 2:
            for k,v in self.expensesdict.items():
                print(f"{k} - {v}")
            edit_ask = input("""
Which part would you like to edit? 
For example if you would like to change the gas input please enter "gas". """)
            new_input = input("Please enter the value you wish to change it to ")
            self.expensesdict[edit_ask] = new_input
        
        elif edit_option == 3:
            for k,v in self.roi.items():
                print(f"{k} - {v}")
            edit_ask = input("""
Which part would you like to edit? 
For example if you would like to change the down payment please enter "down payment". """)
            new_input = input("Please enter the value you wish to change it to ")
            self.roi[edit_ask] = new_input




class Main(): #class that will be running the functions for class Calculator
    def __init__(self):
        self.calculator = Calculator()
        self.options = None

    def opening(self):
        print("""
        Welcome to our Rental Income Calculator!
Wonder if the house you want will be worth renting?
Provide us with a few details and let us do the math for you!
""")

    def run(self):
        self.opening()
        
        self.calculator.cost_of_house()
        while True:
            self.options = self.calculator.input_check("""
Where would you like to go? If you are done with all forms or would like to exit, please enter '6'
        [1] Income
        [2] Expenses
        [3] Cash Flow
        [4] ROI
        [5] Edit
""")
            if self.options == 1:
                self.calculator.income_from_home()
               
            elif self.options == 2:
                self.calculator.expenses_of_home()
                
            elif self.options == 3:
                self.calculator.cash_flow()

            elif self.options == 4:
                self.calculator.return_on_investment()

            elif self.options == 5:
                self.calculator.edit()
            
            elif self.options == 6:
                print("Thank you for using our Rental Income Calculator. Have a great day!")
                break

rental_calc = Main()
rental_calc.run()
