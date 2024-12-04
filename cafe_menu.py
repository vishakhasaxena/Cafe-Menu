menu={"Pizza":100,
      "Pasta":80,
      "Noodles":80,
      "Burger":60,
      "Coffee":50 } 
print("Welcome to the Cafe.")
print("Pizza: Rs100\nPasta: Rs80\nNoodles: Rs80\nBurger: Rs60\nCoffee: Rs50")
total_order=0
# 80+60=
item1 = input("Enter the first order:")
if item1 in menu:
    total_order +=menu[item1] #0+60
    print(f"Your order {item1} is added")
else:
    print("Order something from the menu")
    
another_order=input("Do you want to order another item Yes/No:")
if another_order=="Yes":
    item2= input("Enter your second Order")
    if item2 in menu:
        total_order +=menu[item2] #0+80
        print(f"Your order {item2} is added")
    else:
        print("Order something from the menu")
print(f"Your total order is {total_order}.")
    
    
    


