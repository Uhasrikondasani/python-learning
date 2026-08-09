num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
num_3 = float(input("Enter third number: "))
if num_1 > num_2 and num_3:
    print("The largest number is: ",num_1)
elif num_2 > num_3 and num_1:
    print("The largest number is: ",num_2)
else:
    print("The largest number is: ",num_3)