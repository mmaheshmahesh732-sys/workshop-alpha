def main_menu():
    print(" IVR SYSTEM")
    print("1. Mobile Services")
    print("2. Internet Services") 
    print("3. TV & OTT Services")
    print("4. Talk to Customer Support")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        mobile_menu()
    elif choice == '2':
        internet_menu()
    elif choice == '3':
        tv_ott_menu()
    elif choice == '4':
        print("\nConnecting you to Customer Support... Please wait!")
        input("Press Enter to go back to Main Menu")
        main_menu() # recursive call
    elif choice == '5':
        print("Thank you for calling EKNAL. Have a great day!")
    else:
        print("Invalid choice! Try again.")
        main_menu() # recursive call

def mobile_menu():
    print("MOBILE SERVICES")
    print("1. Prepaid")
    print("2. Postpaid")
    print("3. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        prepaid_menu()
    elif choice == '2':
        postpaid_menu()
    elif choice == '3':
        main_menu() #back to main - recursion
    else:
        print("Invalid choice!")
        mobile_menu()

def prepaid_menu():
    print(" PREPAID ")
    print("1. Balance Inquiry")
    print("2. Recharge")
    print("3. Data Plans")
    print("4. Back")
    print("5. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Your Balance is: Rs. 199.50")
        input("Press Enter to continue")
        prepaid_menu()
    elif choice == '2':
        recharge_menu()
    elif choice == '3':
        data_plans_menu()
    elif choice == '4':
        mobile_menu() # back to mobile
    elif choice == '5':
        main_menu() # back to main
    else:
        print("Invalid choice!")
        prepaid_menu()

def recharge_menu():
    print("RECHARGE")
    print("1. Using Credit Card")
    print("2. Using UPI")
    print("3. Recharge History")
    print("4. Back")
    print("5. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Redirecting to Credit Card payment gateway...")
    elif choice == '2':
        print("Scan UPI QR and complete payment...")
    elif choice == '3':
        print("Last Recharge: Rs. 299 on 20-Sep-2026")
    elif choice == '4':
        prepaid_menu()
    elif choice == '5':
        main_menu()
    else:
        print("Invalid choice!")
    
    input("Press Enter to continue")
    recharge_menu() if choice in ['1','2','3'] else None

def data_plans_menu():
    print("\n--- DATA PLANS ---")
    print("1. 1GB/day")
    print("2. 2GB/day") 
    print("3. Unlimited")
    print("4. Back")
    print("5. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("1GB/day plan activated for Rs. 199")
    elif choice == '2':
        print("2GB/day plan activated for Rs. 299")
    elif choice == '3':
        print("Unlimited plan activated for Rs. 499")
    elif choice == '4':
        prepaid_menu()
    elif choice == '5':
        main_menu()
    else:
        print("Invalid choice!")
    
    input("Press Enter to continue")
    data_plans_menu() if choice in ['1','2','3'] else None

def postpaid_menu():
    print("\n--- POSTPAID ---")
    print("1. Current Bill")
    print("2. Bill Payment")
    print("3. Plan Upgrade")
    print("4. Back")
    print("5. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Your Current Bill: Rs. 599")
    elif choice == '2':
        bill_payment_menu()
    elif choice == '3':
        plan_upgrade_menu()
    elif choice == '4':
        mobile_menu()
    elif choice == '5':
        main_menu()
    else:
        print("Invalid choice!")
    
    input("Press Enter to continue")
    postpaid_menu() if choice in ['1','2','3'] else None

def bill_payment_menu():
    print("\n--- BILL PAYMENT ---")
    print("1. Pay via NetBanking")
    print("2. Pay via Wallet")
    print("3. Back")
    print("4. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Redirecting to NetBanking...")
    elif choice == '2':
        print("Paying via Wallet...")
    elif choice == '3':
        postpaid_menu()
    elif choice == '4':
        main_menu()
    else:
        print("Invalid choice!")
    
    input("Press Enter to continue")
    bill_payment_menu() if choice in ['1','2'] else None

def plan_upgrade_menu():
    print("\n--- PLAN UPGRADE ---")
    print("1. Silver to Gold")
    print("2. Gold to Platinum")
    print("3. Back")
    print("4. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Plan upgraded to Gold successfully!")
    elif choice == '2':
        print("Plan upgraded to Platinum successfully!")
    elif choice == '3':
        postpaid_menu()
    elif choice == '4':
        main_menu()
    else:
        print("Invalid choice!")
    
    input("Press Enter to continue")
    plan_upgrade_menu() if choice in ['1','2'] else None

def internet_menu():
    print("\n--- INTERNET SERVICES ---")
    print("1. Broadband")
    print("2. Fiber")
    print("3. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        broadband_menu()
    elif choice == '2':
        fiber_menu()
    elif choice == '3':
        main_menu()
    else:
        print("Invalid choice!")
        internet_menu()

def broadband_menu():
    print("\n--- BROADBAND ---")
    print("1. Usage Details")
    print("2. Renew Plan")
    print("3. Change Router")
    print("4. Back")
    print("5. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Data Used: 120GB / 500GB")
    elif choice == '2':
        print("1. Monthly Plan  2. Quarterly Plan  3. Yearly Plan")
    elif choice == '3':
        print("1. Request Technician  2. Self Installation Guide")
    elif choice == '4':
        internet_menu()
    elif choice == '5':
        main_menu()
    else:
        print("Invalid choice!")
    
    input("Press Enter to continue")
    broadband_menu()

def fiber_menu():
    print("\n--- FIBER ---")
    print("1. New Connection")
    print("2. Status Check")
    print("3. Back")
    print("4. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("1. Residential  2. Business")
    elif choice == '2':
        print("Your connection status: Active")
    elif choice == '3':
        internet_menu()
    elif choice == '4':
        main_menu()
    else:
        print("Invalid choice!")
    
    input("Press Enter to continue")
    fiber_menu()

def tv_ott_menu():
    print("\n--- TV & OTT SERVICES ---")
    print("1. Channel Packs")
    print("2. Recharge")
    print("3. Complaint")
    print("4. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("1. Sports Pack  2. Movies Pack  3. All-in-One Pack")
    elif choice == '2':
        print("1. 1 Month 2. 6 Months  3. 12 Months")
    elif choice == '3':
        print("1. No Signal  2. Overcharged")
    elif choice == '4':
        main_menu()
    else:
        print("Invalid choice!")
    
    input("Press Enter to continue")
    tv_ott_menu()


main_menu()
