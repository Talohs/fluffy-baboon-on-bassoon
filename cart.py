# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.

# Have a function that takes in user input and returns what that function does
# Have a function that processes those requests 
    #if statements to process the shopping cart responses
# Have a print statement at the end that prints their reicept in a formatted way

shopping_cart = {}
u_choice = input("What would you like to do in the store today?")
def user_resp():
    user_choices = {
        'add': 'add',
        'delete': 'delete',
        'clear': 'clear',
        'show': 'test3',
        'quit': 'quit'
        }
    return user_choices.get(u_choice)

def user_attr():
    hold_cart = {}
    c_choice = user_resp()
    while c_choice != 'quit':
        if c_choice == 'add':
            new_item = input('Please add a food?')
            shopping_cart.update({new_item : new_item})
            item_count = input (f"How many {new_item} would you like?")
            shopping_cart.update({f'number of {new_item}': item_count})
            cost_numeric = 0.0
            for cost_item in new_item:
                cost_numeric += ord(cost_item) * 0.010
            cost_numeric*float(shopping_cart.get(f'number of {new_item}'))
            cost_total = str("%.2f" % cost_numeric)
            shopping_cart.update({f'{new_item} price': cost_total})
            c_choice = input("What would you like to do in the store today?")
            
    return shopping_cart
    
print(user_resp())


# for ct,val in enumerate(user_attr().values()):
#     print("Your reciept\n", f"{val[ct+1]} {val} for ${val}\n")
#     if ct%4 == 0:
#         print('\n')
#     pass
print(shopping_cart)