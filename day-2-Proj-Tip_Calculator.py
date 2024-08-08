print("Welcome to the tip calculator!")
totalbill1=float(input("what was the total bill?"))
tip=int(input("How much tip would you like to give? 10,12,or 15?"))
Total_Person= int(input("How many people to split the bill?"))
billwithtip=(totalbill1)*(tip/100) + totalbill1
totalamount=round(billwithtip,1)
print(totalamount)