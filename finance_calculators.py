# import math 
import math 

#print intial statement // create a variable to hold the multi line string 
# https://www.programiz.com/python-programming/examples/multiline-string#:~:text=You%20can%20use%20'''(,multiline%20string%20as%20shown%20above.

welcome = '''Investment - To calculate the amount of interest you'll earn on your investment. 
Bond - To calculate the amount you'll have to pay on a home loan. 

'''

print(welcome)
# Create a variable to hold the input of the selection // convert all inputs to lowercase 
#https://stackoverflow.com/questions/69443415/how-to-use-input-function-in-multiple-if-statement

financial_product_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()
financial_product = financial_product_input
#create if statement 



if financial_product == "investment": # create if statement for investment condition 
        investment_amount = float(input("How much money are you depositing?"))  # prompt the user to enter investment amount 
        interest_rate =float(input("What is the interest rate amount?")) # prompt the user to enter the interest rate
        r = interest_rate/100 # rate is interest rate / 100 
        investment_time_years = float(input("How many years do you plan on investing for? ")) # prompt the user to enter the investment time (years)
        interest_type = (input("Which interest type do you want? (simple or compound)").lower()) # prompt the user to enter the investment type and convert to lowercase so that all variations are accepted. 

        #Create a nested if statement for the interest type conditions // https://www.tutorialspoint.com/python/nested_if_statements_in_python.htm
        if interest_type == "simple": # condition for simple interest type
                simple = investment_amount *(1 +  (r * investment_time_years)) #simple interest calculation
                print("The total amount with simple interest is " + str(simple))
                print(financial_product_input)

        elif interest_type == "compound":# condition for compound interest type
                compound= investment_amount * math.pow((1+ r),investment_time_years) #compound intrest calculator
                print("The total amount with compund interest is" + str(compound)) 
                
                # https://www.thecalculatorsite.com/finance/calculators/simple-interest-calculator.php  verified the compound and simple calculations   
            
        else: # Print output of incorrect interest type input.
                print("Incorrect interest type!  ")

elif financial_product == "bond":   # Outer Elif statement 
        #Create a nested if statement for the bond repayment conditions
                #added the float type cast so the inputs can be operated on e.g add and divided 
                house_value = float(input("What is the present house value?"))
                interest_rate =float(input("What is the interest rate amount?"))/100
                repayment_time = float(input("What is the repayment time in months? "))
                # created additional variables to simplify the following calculation for the repayment variable
                p = house_value
                i = interest_rate/12
                n = repayment_time

                repayment = (i * p) /(1 - (1 + i)**(-n)) # assigned the calculation to the variable
                print("The total monthly bond repayment  is " + str(repayment)) # converted the repayment variable back to a string so it can be displayed with the string words.
                
                #https://www.ooba.co.za/home-loan/bond-repayment-calculator/ verified calculation on this website 

else: # Print output of incorrect financial product input. 
        print("Incorrect financial product! Please enter Investment or Bond into the calculator.")

