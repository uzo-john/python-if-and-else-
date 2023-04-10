name = input("Hi dear\nKindly Enter your name: ")
print(f"\nwelcome here",name,"to the pizza store\nWhat do you care for!")
print("\n1. big size 4.5kg = NGN8000\n2. medium size 2.5kg = NGN4000\n3. small size 1.5kg = NGN2500")
number = int(input("\nEnter a number from the number 1,2 and 3: "))
if number == 1:
    print("1. big size 4.5kg = NGN8000")
elif number == 2:
    print("2. medium size 2.5kg = NGN4000")
elif number == 3:
    print("3. small size 1.5kg = NGN2500")
else:
    print("You have not made any input.\nPlease",name,"Enter a number")
    
    if number > 3:
        number = int(input("Enter a number from the number 1,2 and 3: "))
    if number == 1:
        print("1. big size 4.5kg = NGN8000")
    elif number == 2:
        print("2. medium size 2.5kg = NGN4000")
    elif number == 3:
        print("3. small size 1.5kg = NGN2500")
print("\nPlease select your preferred type!")
print("\n1. Margherita pizza.\n2. Peppy paneer pizza.\n3. Cheese in corn pizza.\n4. Farmhouse pizza.")
pizza = int(input("\nPlease Enter your preferred type: "))
if pizza == 1:
    print(f"1. Margherita pizza coming up.")
elif pizza == 2:
    print("2. Peppy paneer pizza coming up.")
elif pizza == 3:
    print("3. Cheese in corn pizza coming up.")
elif pizza == 4:
    print("4. Farmhouse pizza coming up.")
else:
    print("wrong input")
print("\nHow was how services",name,)
print("\n1. good 2. bad 3. very good")
result = int(input("\nPlease Enter a preferred option: "))
if result == 1:
    print("Thank you,",name)
elif result == 2:
    print("We will try to improve our services.")
elif result == 3:
    print("Thank you very much")
else:
    print("\nyou have entered a wrong input.")
print("\nDear",name,"Thank you for choosing pizza place.")

