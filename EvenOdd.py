#Program to check if user's number input is Even or Odd

print("Hello, let's check if your number is Even or Odd, please enter only whole Numbers e.g. (1, 2 ,3 ,4 ,10, 17 etc)")
user_number = int(input("Enter your number here: \n"))


if user_number % 2 == 0:
    print(f"Your number {user_number} is Even number! :)")
elif user_number % 2 != 0:
    print(f"Your number {user_number} is Odd number! :)")

print("\n")


#Another alternative solution with function.
def even_odd(n):
    if n % 2 == 0:
        return f"Your number {n} is Even number!"
    else:
        return f"Your number {n} is Odd number!"


#print(even_odd(4))  Call function with number by choice to check what the return statement will be

