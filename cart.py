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

shopping_cart = []
hold_cart = {}
def user_resp(u_choice):
    print(u_choice)
    if u_choice not in ['add', 'delete', 'clear', 'show', 'quit']:
        print("Choice selection are add, delete, clear, show, or quit")
        u_choice = input("What would you like to do in the store today?").lower()
        user_resp(u_choice)
    user_choices = {
        'add': 'add',
        'delete': 'delete',
        'clear': 'clear',
        'show': 'show',
        'quit': 'quit'
        }
    return user_choices.get(u_choice)

def item_cost(item, count):
    cost_numeric = 0.0
    for cost_item in item:
        cost_numeric += ord(cost_item) * 0.010
    cost_numeric*float(count)
    cost_total = str("%.2f" % cost_numeric)
    # shopping_cart.update({f'{item} price': cost_total})
    return cost_total

def choice_add():
    add_cart = {}
    new_item = input('Please add a food?')
    shopping_cart.append(new_item)
    item_count = input (f"How many {new_item} would you like?")
    add_cart.update({f'number of {new_item}': item_count})
    item_total = item_cost(new_item, item_count)
    add_cart.update({f'cost of {new_item}': item_total})
    shopping_cart.append(add_cart)
    print(shopping_cart)
    # return add_cart

# def choice_del():
#     rid_me = input("What item would you like to remove?")
#     if rid_me in shopping_cart:
#         shopping_cart[shopping_cart.index(rid_me):shopping_cart.index(rid_me)+2]
#     else:
#         print("You haven't bought any of those yet")
    
def user_attr():
    c_choice = user_resp(input("What would you like to do in the store today?").lower())
    while c_choice != 'quit':
        if c_choice == 'add':
            choice_add()
            print(shopping_cart)
            # hold_cart.update(choice_add(hold_cart).copy())
            # print(choice_add(hold_cart).copy())
            c_choice = user_resp(input("What else would you like to do in the store today?"))
        elif c_choice == 'clear':
            shopping_cart.clear()
        elif c_choice == 'delete'
            # choice_del()        
    return hold_cart
    
# print(user_resp())
# user_resp(input("What would you like to do in the store today?"))
user_attr()
for ct,val in enumerate(shopping_cart):
    if isinstance(val, str):
        item = val
        nums = [num for num in shopping_cart[ct+1].values()]
        print(f"{nums[0]} {item} for ${nums[1]}")

        
    # print(ct, val,)
    # print("Your reciept\n", f"{val[ct+1].get(f'number of {val}')} {val} for ${val[ct+1].get(f'cost of {val}')}\n")

print(shopping_cart)