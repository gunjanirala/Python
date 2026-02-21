Print_what=input("Type what you want to print:")
print(Print_what)
flag=0
while flag==0:
    user_input=input("Do you want to print something else? (yes/no): ")
    if user_input.lower() == "yes":
        Print_what_else=input("Type what you want to print:")
        print(Print_what_else)
    elif user_input.lower() == "no":
        flag=1
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
