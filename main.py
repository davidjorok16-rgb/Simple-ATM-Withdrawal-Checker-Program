Accountbalance= float(input("Account balance: $"))
Withdrawal= float(input("Withdrawal amount: $"))
if(Withdrawal<=0):
    print("REJECTED")
elif(Withdrawal>Accountbalance):
    print("REJECTED")
else:
    print(f"Remaining Balance: ${Accountbalance-Withdrawal:.2f}")