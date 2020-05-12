#definitions
restart = ("y")
chances = 3
balance = 100.00
Ibalance = 0



#Welcome message
print("******************************************************************")
print("******************************************************************")
print("Hello and welcome to this automated ATM program...")
print("this program is designed to allow you to check you balance,")
print("withdraw money and also deposit money into your account")
print("*******************************************************************")
print("*******************************************************************")
# Screen/task after card is inserted
PIN = int(input("Please enter your PIN-"))
if PIN == (5981):
    print("PIN verified\n")
    while restart not in ("n", "NO", "no", "N"):

        #Menu
        print("************************************")
        print("Welcome to this ATM, what would you like to do?")
        print("1. View balance")
        print("2. Withdraw cash")
        print("3. Pay an account")
        print("4. View recent transactions")
        print("5. Change PIN")
        print("6. Other")
        option = int(input("Choose a number-"))
        if option == 1:  #Option 1
            print("Your balance is £", balance, "\n")
            restart = input("Would you like to use another service? (Y/N)")
            if restart in ('n', 'NO', 'no', 'N'):
                print('Thank You')
                break
        elif option == 2:  #Option 2
            option2 = ("y")
            withdrawl = float(
                input(
                    "How much would you like to withdraw from your account? In terms in 5 up to £50 then it would be £100 -"
                ))
            if withdrawl in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 100]:
                balance = balance - withdrawl
            print("your balance is now £", balance)
            restart = input("Would You you like to use another service? (Y/N)")
            if restart in ('n', 'NO', 'no', 'N'):
                print('Thank You')
                break
        elif option == 3:  #option 3
            Pay_An_Account = int(
                input("How much would you like to add to the account?"))
            balance = balance + Pay_An_Account
            print("After paying in the account balance is now-", balance)
            restart = input("Would you like to use another service? (Y/N)")
            if restart in ('n', 'NO', 'no', 'N'):
                print('Thank You')
                break
        elif option == 4:  #option 4
            print("Please enter your 2FA code to accsess this data-")
            PIN2 = int(input("2FA-"))
            if PIN2 == (5765):
                #recent transactions
                print("************************************")
                print("Recent transactions- In the last 7 days")
                print("************************************")
                print("Tesco - £45.00")
                print("KFC - £2.40")
                print("Asda- £200")
                print("CEX- £40")
                print("Barclays- £100")
                print("Ticketmaster UK - £145")
                print("************************************")
            else:
                print("Unknown 2FA Code")
                restart = input("Would You you like to use another service? (Y/N)")
                if restart in ('n', 'NO', 'no', 'N'):
                  print('Thank You')
                  break
        elif option == 6:  
            #Menu
          print("************************************")
          print("Welcome to Other, what would you like to do?")
          print("1. Top-up a mobile")
          print("2. Close an account")
          print("3. Support")
          option = int(input("Choose a number-"))
          if option == 1: #Mobile top-up
            mobile = int(input("Type your phone number-"))
            MBalance = int(
                input("How much would you like to add to the account?-"))
            MBalance = Ibalance + MBalance
            Tbalance = balance - MBalance
            print("After paying your mobile balance is now- £", MBalance)
            print("******************************")
            print("******************************")
            print("Your account balance is now- £", Tbalance)
            restart = input("Would you like to use another service? (Y/N)")
            if restart in ('n', 'NO', 'no', 'N'):
                print('Thank You')
                break
          elif option == 2:
            #closing account
              print("Closing account.....")
              print("*************10%**************")
              print("******************************")
              print("******************************")
              print("*************30%**************")
              print("******************************")
              print("*************50%**************")
              print("******************************")
              print("*************75%**************")
              print("******************************")
              print("*************90%**************")
              print("******************************")
              print("************DONE**************")
              









                  
        #elif option == 5:  #option 5
         #def validatePIN(pin):
          #attempt=input("Please enter your 4-digit PIN: ")
        #count=1
    #while (attempt != pin) and (count<3):
      #attempt=input("Please enter your 4-digit PIN: ")
    #count+=1
    #if (attempt == pin):
     #   return True
    #print("Invalid PIN - Account Blocked")
    #return False

    #def CP(pin):
     # if validatePIN(pin):
      #  pin=input("Please enter your new PIN: ")
       # print("Thank you. Your new PIN is: ",pin)
      #return pin

    #pin = CP('5981')
    #restart = input("Would you like to use another service? (Y/N)")
    #if restart in ('n', 'NO', 'no', 'N'):
    # print('Thank You')
  #break










else:
 print("incorrect PIN remove card and try again.. 2 attempts left")
 input("\nPress Enter to return card ^^ ---")
 print("Thank you for using this ATM... Goodbye")
######################################
