# loan payment calculation
money_owed=float(input("how much money is owed:\n"))
apr=float(input("anual percentage rate:\n"))
payment=float(input("how much you will pay monthly:\n"))
months=int(input("how many months to pay loan:/n"))

#montly intrest cal
monthly_rate=apr/100/12

for i in range(months):

    #intrest to pay 

    intrest_rate= money_owed*monthly_rate

    money_owed=money_owed+intrest_rate

    if (money_owed - payment < 0):
        print("the last month money owed:\n", money_owed)
        print("no.of months to complete:\n", i+1)
        break

    #payment 

    money_owed= money_owed - payment 

    print("payment of", payment, "of intrest", intrest_rate )
    print("money owed as of now:", money_owed)

