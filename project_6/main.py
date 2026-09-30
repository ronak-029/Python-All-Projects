#  Expence Tracker build in python 

expnsesList = []
print("Welcome To expence Tracker : khrcha Kam Karo")

while True:
    print("===MENU===")
    print("1. Add Expense ")
    print("2. view All Expaneces ")
    print("3. View Total Khrcha")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))

    if(choice == 1):
        date = input("Enter Today Date : ")
        category = input("Enter Your Khrcha kaha kaha kiya hai bro (rent , food , Travel , car , books etc ) : ")
        amount = float(input("Acha Chal bata Total Khrcha kitna kiya =  "))

        expence = {
            "date" : date,
            "category" : category,
            "amount" : amount
        }

        expnsesList.append(expence)
        print("\n =====Khrcha added succesfully======")

    # View all Khrcha     
    if(choice == 2):
        if(expnsesList == 0):
            print("Bhai khrcha tho kuch kiya hi nhi . ")
            
        else:
            print("====bhai Itna krcha===")
            count = 1
            for eachkhrcha in expnsesList:
                print(f"{count} => {eachkhrcha["date"]},{eachkhrcha["category"]}, and Total Khrcha is : {eachkhrcha["amount"]}")
                count += 1

    # View total Khrcha 

    if(choice == 3):
        total = 0
        for eachkhrcha in expnsesList:
            total = total + eachkhrcha["amount"]

            print(f"total amount is : {total}")
            print("\n ====Itna Khrcha bhai pasie bachoooo====")

    # for exit 

    elif(choice == 4):
        print("================Thankyou aapne hamra System Use Kiya================ ")
        break

    else:
        print("please Enter Correct number ")
        print("==========Try again==============")
