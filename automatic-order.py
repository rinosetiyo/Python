# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    small_pizza = 15
    if add_pepperoni == "Y":
        pepperoni = 2
        total = small_pizza + pepperoni
        if extra_cheese == "Y":
            small_pizza = 15
            cheese = 1
            pepperoni = 2
            extra = small_pizza + pepperoni + cheese
            print(f"Your final bil is ${extra}.")
        else:
            print(f"Your final bill is ${total}.")
    elif add_pepperoni != "Y" and extra_cheese == "Y":
        small_pizza = 15
        cheese =1
        not_extra = small_pizza + cheese
        print(f"Your final bill is ${not_extra}.")
    else:
        print(f"Your final bill is ${small_pizza}.")
elif size == "M":
    medium_pizza = 20
    if add_pepperoni == "Y":
        pepperoni = 3
        total = medium_pizza + pepperoni
        if extra_cheese == "Y":
            medium_pizza = 20
            cheese = 1
            pepperoni = 3
            extra = medium_pizza + pepperoni + cheese
            print(f"Your final bill is ${extra}.")
        else:
            print(f"Your final bill is ${total}.")
    elif add_pepperoni != "Y" and extra_cheese == "Y":
        medium_pizza = 20
        cheese =1
        not_extra = medium_pizza + cheese
        print(f"Your final bill is ${not_extra}.")
    else:
        print(f"Your final bill is ${medium_pizza}.")
elif size == "L":
    large_pizza = 25
    if add_pepperoni == "Y":
        pepperoni = 3
        total = large_pizza + pepperoni
        if extra_cheese == "Y":
            large_pizza = 25
            cheese = 1
            pepperoni = 3
            extra = large_pizza + pepperoni + cheese
            print(f"Your final bill is ${extra}.")
        else:
            print(f"Your final bill is ${total}.")
    elif add_pepperoni != "Y" and extra_cheese == "Y":
        large_pizza = 25
        cheese =1
        not_extra = large_pizza + cheese
        print(f"Your final bill is ${not_extra}")
    else:
        print(f"Your final bill is ${large_pizza}")
else:
    print("Invalid input or Missing input")
