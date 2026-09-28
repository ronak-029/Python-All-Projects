# Rent Calculator 

rent = int(input("Enter Your Hostel/Flat Rent : "))
food = int(input("enter the Amount Of food you Odered This mounth : "))
electrictiy_spend = int(input("Enter the total electrictiy spend : "))
charge_per_unit = int(input("enter Charge Per Unit : "))
persons = int(input("Enter the number of person living in Flat/room :  "))
total_bill = electrictiy_spend*charge_per_unit
sum = (rent + food + total_bill)/persons

print(f"The Divided Rent in all Of you is {sum}")