#08-26-21
#NATE, NIKKA C.
#REGALA, JHON RAYMOND S.
#CCS 1101 - CSAA
#TUITION

print("TUITION PROGRAM")
tuition = int(input("Enter Tuition: "))

# TUITION CANNOT BE LESS THAN P5000
if tuition < 5000:
    print("Input amount that is less than P5,000 is not allowed.")
    
# MODE OF PAYMENT
else:
    option = float(input("Select an option \n [1] Full Payment - 20% Discount \n [2] Installment A - 5% Interest \n [3] Installment B - 10% Interest \n [Press 1, 2, or 3 only] \n Enter Mode of Payment: " ))
    
    # FULL PAYMENT
    if option == 1:
        full_payment =  tuition - (tuition * .20) 
        print("You are going to pay P{0:,.2f} tuition.".format(full_payment))
        
    # INSTALLMENT A
    elif option == 2:
        installment_a = tuition + (tuition* 0.05)
        print('You are going to pay P{0:,.2f} tuition' .format(installment_a ))
        
    # INSTALLMENT B
    elif option == 3:
        installment_b = tuition + ( tuition * 0.10)
        print('You are going to pay P{0:,.2f} tuition' .format(installment_b ))
        
    # WRONG MODE OF PAYMENT
    else:
        print("Wrong mode of payment. Please input from 1 - 3 only.")