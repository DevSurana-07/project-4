print("Welcome to the Data Analyzer and Transformer Program !\n")
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)
on = True
while on:
    choice = int(input("1. Input Data\n 2. Display Data Summary (Built - in Functions)\n 3. Calculate Factorial (Recursion)\n 4. Filter Data by Threshold (Lambda Function)\n 5. Sort Data\n 6.Display Dataset Statistics (Return Multiple Values)\n 7. Exit Program\n Please enter your choice : "))
    if choice == 1:
        arr = []
        n = int(input("Enter the numbers : "))
        for i in range(n):
            elem = int(input("Enter the elem:-- "))
            arr.append(elem)
        print("Data has been stored successfully !\n ")
    elif choice == 2:
        pass
    
    elif choice == 3:
        num = int(input("\nEnter a number to calculate its factorial : "))
        result = factorial(num)
        print(f"\nFactorial of {num} is : {result}\n")
    elif choice == 4:
        pass
    elif choice == 5:
        options = int(input("\nChoose sorting option :\n 1.Ascending\n  2.Decending\n Enter your choice :\n "))
        if options == 1:
            arr.sort()
            print(arr)
        elif options == 2:
            print(sorted(arr))
        else:
            print("You have entered the wrong option ")
    elif choice == 6:
        pass
    elif choice == 7:
        print("Thank you for choosing the Data Analyzer and Transformer Program. Goodbye !")
        on= False
    else:
        print("You have entered the wrong choice : ")
        on = False
    
