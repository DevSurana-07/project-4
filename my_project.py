print("Welcome to the Data Analyzer and Transformer Program !\n")
while True:
    choice = int(input("Main Menu:\n 1.Input Data\n 2.Display Data Summary (Built-in Functions)\n 3.Calculate Factorial(Recursion)\n 4.Filter Data by Threshold (Lambda Fumctions)\n 5.Sort Data\n 6.Display Dataset statistics(Return Multiple Values)\n 7.Exit Program\n Please enter your choice: "))
    def factorial (num):
        if num <= 1:
            return 1
        else:
            return num*factorial(num-1)
    def statistics(arr):
        minimum = min(arr)
        maximum = max(arr)
        add = sum(arr)
        avg = sum(arr)/len(arr)
        return minimum,maximum,add,avg

    if choice == 1:
        arr = []
        n = int(input("Enter the number :- "))
        for i in range(n):
            arr.append(int(input("Enter the element : ")))
        print("\nData has been stored successfully !\n")
    elif choice == 2:
        print("\nData Summary :")
        print("-Toltal elements :",arr)
        print("-Minimum Value :",min(arr))
        print("-Maximum Value :",max(arr))
        print("-Sum of all value :",sum(arr))
        print("-Average Value :",sum(arr)/len(arr))
        print("\n")
    elif choice == 3:
        fact = int(input("Enter a number to calculate its factorial : "))
        fact1 = factorial(fact)
        print(f"Factorial of {fact} is : {fact1}\n")
    elif choice == 4:
        abc = int(input("Enter a threshold value to filter out data below this value : "))
        bca = lambda val : [i for i in arr if i>val]
        print(f"Filtered Data (values >= {abc}): {bca(abc)}")
    elif choice == 5:
        option =int(input("Choose sorting option :\n 1.Ascending Order\n 2.Decending Order\n Please enter your choice:"))
        if option == 1:
            print(f"The Ascending order is :",sorted(arr))
        elif option == 2:
            print(f"The Decending order is :{sorted(arr,reverse = True)}")
    elif choice == 6:
        min,max,add,avg=statistics(arr)
        print("Dataset Statistics:")
        print(f"-Minimum value : {min}")
        print(f"-Maximum value : {max}")
        print(f"-Sum of all value : {add}")
        print(f"-Average value : {avg}")
    elif choice == 7:
        print("Exiting the program Goodbye ! ")
        break
    else:
        print("\nYou have entered the wrong choice !\n")
        break