print("---MENU---\n---MAIN DISH---\nidly----------5\ndosa---------20\nchappati-----20\nparota-------10\n---SIDE DISH---\nkadai------110\nvegkurma---100\nchanna-----100")
main_dish = {100: ('idly', 5),101: ('dosa', 20),102: ('chappati', 20),103: ('parota', 10)}
side_dish = {200: ('kadai', 110),201: ('vegkurma', 100),202: ('channa', 100)}

while True:
    try:
        order = input("TAKE YOUR ORDER (y/n)(d for develop):")
        if order == "y":
            print("Place Order.")
            print("\n---MAIN DISH AND SIDE DISH---")
        elif order == 'n':
            print("Order not taken")
            break
        elif order == 'd':
            try:
                dev=input("To add new dishes in menu press(a) & to delete(f):")
                i=input("If in main dish press(m) or side dish press(s):")
                if i == 'm':
                    if dev == 'a':
                        key=int(input("Enter item code:"))
                        dish=input("Dish name:")
                        price=int(input("Price of dish:"))
                        main_dish[key]=(dish,price)
                        print("Item added")
                        print(main_dish)
                    elif dev == 'f':
                        key=int(input("enter code to delete:"))
                        if key in main_dish:
                            del main_dish[key]
                            print("Item deleted")
                            print(main_dish)
                        else:
                            print("Item not found")
                elif i == 's':
                    if dev == 'a':
                        key=int(input("Enter item code:"))
                        dish=input("Dish name:")
                        price=int(input("Price of dish:"))
                        side_dish[key]=(dish,price)
                        print("Item added")
                        print(side_dish)
                    elif dev == 'f':
                        key=int(input("enter code to delete:"))
                        if key in side_dish:
                            del side_dish[key]
                            print("Item deleted")
                            print(side_dish)
                        else:
                            print("Item not found")
                else:
                    raise ValueError
            except ValueError:
                print("not valid")
        else:
            raise ValueError
    except ValueError:
        print("Invalid Input")
        
        
    break

    

#take order

order=[]
def take_order():
    while True:
        try:
            key=int(input("Enter item Code(To End press 0):"))
            # for kei in main_dish.keys():
            #      map(int,str(kei))     
            if key in main_dish:
                dish,price=main_dish[key]
                print(f"Dish:{dish}  Price:{price}")
            elif key in side_dish:
                dish,price=side_dish[key]
                print(f"Dish:{dish}  Price:{price}")
            if key == 0:
                break
            if key in main_dish or key in side_dish:
                    quan=int(input("Enter Quantity:"))
                    order.append((key,quan))    
            else:
                    raise ValueError
        except ValueError:
                print("Invalid Input.Try Again.")
take_order()

##billing
total=0
print("\n---BILL---")
for key,quan in order:
    if key in main_dish:
        dish,price=main_dish[key]
    else:
        dish,price=side_dish[key]
    tot=price*quan
    print(f"{dish} x {quan} = {tot}")
    total += tot
print(f"Total: {total}")

