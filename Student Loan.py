
def loan_eligibility():
    Emp = input("Employment Status (student/non-student): ")

    if Emp == "student":
        c_income = int(input('Enter your current income:'))
        c_score = int(input('Enter your credit score: '))
        o_obli = int(input("Enter any outstanding obligations: "))
        age1 = int(Age)

        if c_income <= 2000 and c_score <= 580 and o_obli >= 1000:
            print("You are not eligible for any loan facility at the moment due to low income.")
        elif c_income <= 4000 and c_score <= 670 and o_obli >= 3000:
            print("You are not eligible for a loan at the moment due to high obligations.")
        elif c_income <= 6000 and c_score <= 740 and o_obli >= 10000:
            print("You are not eligible for a loan at the moment due to high obligations.")
        elif c_income <= 8000 and c_score <= 800 and o_obli >= 20000:
            print("You are not eligible for a loan at the moment due to high obligations.")
        else:
            print("You are eligible for a loan at this time.")
    elif Emp == "non-student":
        # Handle non-student eligibility criteria
        Emp1 = input("Enter your specific employment:")
        c_income1 = int(input('Enter your current income:'))
        c_score1 = int(input('Enter your credit score: '))
        o_obli1 = int(input("Enter any outstanding obligations: "))
        age2 = int(Age)

        if c_income1 <= 20000 and c_score1 <= 580 and o_obli1 >= 10000:
            print("You are not eligible for any loan facility at the moment due to low income.")
        elif c_income1 <= 40000 and c_score1 <= 670 and o_obli1 >= 25000:
            print("You are not eligible for a loan at the moment due to high obligations.")
        elif c_income1 <= 60000 and c_score1 <= 740 and o_obli1 >= 30000:
            print("You are not eligible for a loan at the moment due to high obligations.")
        elif c_income1 <= 80000 and c_score1 <= 800 and o_obli1 >= 40000:
            print("You are not eligible for a loan at the moment due to high obligations.")
        else:
            print("You are eligible for a loan at this time.")

    else:
        print("Invalid employment status.")

name = input('Enter Name:')
Age = input('Enter Age:')

loan_eligibility()
