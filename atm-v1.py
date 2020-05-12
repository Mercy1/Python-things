#Welcome message
print ("******************************************************************")
print ("******************************************************************")
print("Hello and welcome to this automated ATM program... this program is designed to allow you to check you balance, withdraw money and also deposit money into your account in a few easy steps, please enter your card to get started ^^")
print ("*******************************************************************")
print ("*******************************************************************")
# Screen/task after card is inserted
PIN = int (input("Please enter your PIN-"))
if PIN == 4764 :
  print ("Welcome user to this ATM, what would you like to do?")
  print ("1. View balance")
  print ("2. Withdraw cash")
  print ("3. Top-up mobile")
  print ("4. Other")
else: 
  print ("incorrect PIN remove card and try again..")
input("\nPress C to return card ^^ ---")
print ("Goodbye ^^")
######################################
