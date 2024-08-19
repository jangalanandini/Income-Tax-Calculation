import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

def tax_calculation():
    print("\t\t\t*************** WELCOME TO THE INCOME TAX CALCULATION PORTAL *************** \n")
    print(" \t\t\t Please follow the Instructions mentioned \n\n")
    
    User_income = eval(input("\t\t\t Enter the INCOME Of the person: "))

    if User_income <= 250000:
        tax_income = 0
        print("\t\t\t No Need To pay any Taxes ")
    elif 250001 <= User_income <= 500000:
        tax_income = (User_income - 250000) * 0.05
        print("\t\t\t Tax to be paid is", tax_income)
    elif 500001 <= User_income <= 750000:
        tax_income = (User_income - 500000) * 0.1 + 12500
        print("\t\t\t Tax to be paid is", tax_income)
    elif 750001 <= User_income <= 1000000:
        tax_income = (User_income - 750000) * 0.15 + 37500
        print("\t\t\t Tax to be paid is", tax_income)
    elif 1000001 <= User_income <= 1250000:
        tax_income = (User_income - 1000000) * 0.2 + 75000
        print("\t\t\t Tax to be paid is", tax_income)
    elif 1250001 <= User_income <= 1500000:
        tax_income = (User_income - 1250000) * 0.25 + 125000
        print("\t\t\t Tax to be paid is", tax_income)
    else:
        tax_income = (User_income - 1500000) * 0.3 + 187500
        print("\t\t\t Tax to be paid is", tax_income)

    print("\t\t\t Are you Eligible For Student Loan if YES Press 1 : ")
    choice = eval(input("\t\t\t Enter Your Choice : "))
    student_ded_income = 0
    if choice == 1:
        Student_loan = eval(input("\t\t\t Enter the Student Loan amount: "))
        if Student_loan > 0 and Student_loan <= 500000:
            print("\t\t\t No Deductions Included")
        elif 500001 <= Student_loan <= 900000:
            student_ded_income = (Student_loan - 500001) * 0.07
            print("\t\t\t The Amount Deducted is", round(student_ded_income, 2))
        elif 900001 <= Student_loan <= 1650000:
            student_ded_income = (Student_loan - 900001) * 0.12
            print("\t\t\t The Amount Deducted is", round(student_ded_income, 2))
        elif 1650001 <= Student_loan <= 2100000:
            student_ded_income = (Student_loan - 1650001) * 0.15
            print("\t\t\t The Amount Deducted is", round(student_ded_income, 2))
        elif 2100001 <= Student_loan <= 2650000:
            student_ded_income = (Student_loan - 2100001) * 0.17
            print("\t\t\t The Amount Deducted is", round(student_ded_income, 2))
        elif 2650001 <= Student_loan <= 3200000:
            student_ded_income = (Student_loan - 2650001) * 0.19
            print("\t\t\t The Amount Deducted is", round(student_ded_income, 2))
        else:
            student_ded_income = (Student_loan - 3200000) * 0.2
            print("\t\t\t The Amount Deducted is", round(student_ded_income, 2))

    print("\t\t\t Are you Eligible For Home Loan if YES Press 1 : ")
    choice = eval(input("\t\t\t Enter Your Choice : "))
    home_ded_income = 0
    if choice == 1:
        Home_loan = eval(input("\t\t\t Enter the Home Loan amount: "))
        if Home_loan > 0 and Home_loan <= 400000:
            print("\t\t\t No Deductions Included")
        elif 400001 <= Home_loan <= 700000:
            home_ded_income = (Home_loan - 400001) * 0.05
            print("\t\t\t The Amount Deducted is", round(home_ded_income, 2))
        elif 700001 <= Home_loan <= 1050000:
            home_ded_income = (Home_loan - 700001) * 0.075
            print("\t\t\t The Amount Deducted is", round(home_ded_income, 2))
        elif 1050001 <= Home_loan <= 1250000:
            home_ded_income = (Home_loan - 1050001) * 0.09
            print("\t\t\t The Amount Deducted is", round(home_ded_income, 2))
        elif 1250001 <= Home_loan <= 1500000:
            home_ded_income = (Home_loan - 1250001) * 0.1
            print("\t\t\t The Amount Deducted is", round(home_ded_income, 2))
        elif 1500001 <= Home_loan <= 1750000:
            home_ded_income = (Home_loan - 1500001) * 0.105
            print("\t\t\t The Amount Deducted is", round(home_ded_income, 2))
        else:
            home_ded_income = (Home_loan - 1750001) * 0.11
            print("\t\t\t The Amount Deducted is", round(home_ded_income, 2))

    print("\t\t\t Are you Eligible For Provident fund if YES Press 1 :")
    choice = eval(input("\t\t\t Enter the Choice : "))
    pf_ded_income = 0
    if choice == 1:
        pf = eval(input("\t\t\t Enter the Provident Fund Amount : "))
        if pf > 0 and pf <= 30000:
            print("\t\t\t No Deductions Included")
        elif 30001 <= pf <= 37500:
            pf_ded_income = (pf - 30001) * 0.07
            print("\t\t\t The Amount Deducted is", round(pf_ded_income, 2))
        elif 37501 <= pf <= 42000:
            pf_ded_income = (pf - 37501) * 0.07
            print("\t\t\t The Amount Deducted is", round(pf_ded_income, 2))
        elif 42001 <= pf <= 47000:
            pf_ded_income = (pf - 42000) * 0.07
            print("\t\t\t The Amount Deducted is", round(pf_ded_income, 2))
        elif 47001 <= pf <= 63000:
            pf_ded_income = (pf - 47000) * 0.07
            print("\t\t\t The Amount Deducted is", round(pf_ded_income, 2))

    print("\t\t\t Are you Eligible for any LIC POLICY if YES Press 1 :")
    choice = eval(input("\t\t\t Enter the Choice : "))
    lic_ded_income = 0
    if choice == 1:
        lic_policy = eval(input("\t\t\t Enter the LIC POLICY Amount : "))
        if lic_policy > 0 and lic_policy <= 50000:
            print("\t\t\t No Deductions Included")
        elif 50001 <= lic_policy <= 150000:
            lic_ded_income = (lic_policy - 50001) * 0.1
            print("\t\t\t The Amount Deducted is", round(lic_ded_income, 2))
        elif 150001 <= lic_policy <= 300000:
            lic_ded_income = (lic_policy - 150001) * 0.115
            print("\t\t\t The Amount Deducted is", round(lic_ded_income, 2))
        elif 300001 <= lic_policy <= 450000:
            lic_ded_income = (lic_policy - 300001) * 0.125
            print("\t\t\t The Amount Deducted is", round(lic_ded_income, 2))
        else:
            lic_ded_income = (lic_policy - 450000) * 0.13
            print("\t\t\t The Amount Deducted is", round(lic_ded_income, 2))

    total_deductions = student_ded_income + home_ded_income + pf_ded_income + lic_ded_income
    final_tax = tax_income - total_deductions
    print("\t\t\tThe total deductions are:", total_deductions)
    print("\t\t\tThe final tax after deductions is:", final_tax)

    name = str(input("\t\t\t Enter your name: "))
    age = int(input("\t\t\t Enter your Age: "))
    phone_num = int(input("\t\t\t Enter Your Phone Number: "))
    aadhar_num = int(input("\t\t\t Enter Your Aadhar Number: "))

    data = {
        "Name": [name],
        "Age": [age],
        "Phone Number": [phone_num],
        "Aadhar Number": [aadhar_num],
        "User Income": [User_income],
        "Tax": [tax_income],
        "Total Deductions": [total_deductions],
        "Final Tax": [final_tax]
    }

    df = pd.DataFrame(data)
    df.to_csv("year_tax.csv", mode="a", header=False, index=False)
    print("\t\t\t Your data has been saved successfully.")

def clustering():
    # Load the dataset
    dataset = pd.read_csv("year_tax.csv")
    
    # Extract values for clustering
    X = dataset.iloc[:, :].values
    
    # Plot the dendrogram
    dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
    
    # Set the plot title and labels
    plt.title("Dendrogram")
    plt.xlabel("Countries")
    plt.ylabel("Euclidean distance")
    
    # Display the plot
    plt.show()

# Call the tax_calculation function
tax_calculation()

# Call the clustering function
clustering()
