#for this first project i'm going to make an expense tracker using the skills i've learned so far
#task 1, welcome the user, ask for thei name

wel_name = input("Enter your name:")
print("Welcome,", wel_name + "!", "Let's track your expenses")

#task 2 is asking for number of expenses
numexpenses = int(input("Enter the number of expenses: "))

expenses = []
#task 3 is to make a list and append it

for i in range(numexpenses):
    amount = int(input(f"Enter expense {i + 1}: "))
    expenses.append(amount)

if numexpenses <= 0:
    print("please enter values greater than 0")
else:
        
    total = sum(expenses)
    average = round(total / len(expenses), 2)
        
    #task 4 calculate the total

    print("\n======Expense Summary======")

    print ("total spent Rs:",total)

    #task 5 caculating the average which is the sum of all numbers/the total numbers
    print("your average is Rs:",average)

    #task 6 calculating the smallest and largest expense
    smallest = min(expenses)
    largest = max(expenses)
    print("Smallest expense Rs:",smallest)
    print("Largest expense Rs:",largest)
        
        
