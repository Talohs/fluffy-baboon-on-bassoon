
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

shopping_cart = ['bananas', {'number of bananas': '5', 'cost of bananas': '6.92'}, 'apples', {'number of apples': '3', 'cost of apples': '6.13'}, 'pears', {'number of pears': '10', 'cost of pears': '5.07'}]
hold_cart = {}
total_cost = 18.12
def user_resp(u_choice):
    if u_choice not in ['add', 'delete', 'clear', 'show', 'quit']:
        print("Choice selection are add, delete, clear, show, or quit")
        u_choice = input("What would you like to do in the store today? Choice selection are add, delete, clear, show, or quit").lower()
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
    global total_cost
    cost_numeric = 0.0
    for cost_item in item:
        cost_numeric += ord(cost_item) * 0.010
    cost_numeric*float(count)
    cost_total = str("%.2f" % cost_numeric)
    total_cost += cost_numeric
    return cost_total

def choice_add():
    add_cart = {}
    new_item = input('What would you like to buy?')
    shopping_cart.append(new_item)
    item_count = input (f"How many {new_item} would you like?")
    add_cart.update({f'number of {new_item}': item_count})
    item_total = item_cost(new_item, item_count)
    add_cart.update({f'cost of {new_item}': item_total})
    shopping_cart.append(add_cart)


def choice_del():
    global total_cost
    global shopping_cart
    rid_me = input("What item would you like to remove?").lower()
    if rid_me in shopping_cart:
        total_cost -= float(shopping_cart[shopping_cart.index(rid_me)+1].get(f'cost of {rid_me}'))
        shopping_cart = shopping_cart[:shopping_cart.index(rid_me)] + shopping_cart[shopping_cart.index(rid_me)+2:]
    else:
        print("You haven't bought any of those yet")

def print_out():
    for ct,val in enumerate(shopping_cart):
        if isinstance(val, str):
            item = val
            nums = [num for num in shopping_cart[ct+1].values()]
            print(f"{nums[0]} {item.title()} for ${nums[1]}")
    print(f'${"%.2f" % total_cost}')

    
def user_attr():
    global total_cost
    c_choice = user_resp(input("What would you like to do in the store today? Choice selection are add, delete, clear, show, or quit").lower())
    while c_choice != 'quit':
        if c_choice == 'add':
            choice_add()
            c_choice = user_resp(input("What else would you like to do in the store today? Choice selection are add, delete, clear, show, or quit").lower())
        elif c_choice == 'clear':
            shopping_cart.clear()
            total_cost = 0.00
            c_choice = user_resp(input("What else would you like to do in the store today? Choice selection are add, delete, clear, show, or quit").lower())
        elif c_choice == 'delete':
            choice_del()
            c_choice = user_resp(input("What else would you like to do in the store today? Choice selection are add, delete, clear, show, or quit").lower())
        elif c_choice == 'show':
            print_out()
            c_choice = user_resp(input("What else would you like to do in the store today? Choice selection are add, delete, clear, show, or quit").lower())
    return hold_cart
    
user_attr()
print("Your Reciept")
print_out()

