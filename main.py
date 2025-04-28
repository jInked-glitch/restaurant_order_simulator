menu = {
    "coffee":{"price": 1.50, "stock": 10},
    "tea":{"price": 3, "stock": 15},
    "juice":{"price": 3.50, "stock": 8}
}

total_user_order = {}

for item in menu:
    print(f"{item} - €{menu[item]['price']}")

on_going = True
while on_going:
    user_order = input("What would like to order? \n").lower()
    if user_order == "exit":
        total_price = 0
        print(f"Thanks for your order! Here’s a summary of your order:")
        for item, qty in total_user_order.items():
            price = menu[item]["price"]
            total_price += price * qty
            print(f"{item} x{qty} - €{price * qty}")
        print(f"Total: €{total_price}")
        on_going =  False
    elif user_order not in menu:
        print(f"Sorry, we don't have {user_order} in our menu.")
# stock_check
    elif menu[user_order]['stock']> 0:
        print(f"Here is your order: {user_order} - €{menu
        [user_order]['price']}")
        print("Do you want to order anything else? What would like to order? If not, please input 'exit'.")
        menu[user_order]['stock'] -= 1
        # 辞書に記録
        if user_order in total_user_order:
            total_user_order[user_order] += 1
        else:
            total_user_order[user_order] = 1
    else:
        print(f"Sorry, no more stock of {user_order}.")
        


