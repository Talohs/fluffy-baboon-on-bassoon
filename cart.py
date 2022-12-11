
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
total_cost = 0.00
def user_resp(u_choice):
    if u_choice not in ['add', 'delete', 'clear', 'show', 'quit']:#junk collector
        print("Choice selections are add, delete, clear, show, or quit")
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
    """
    This function takes in an item to buy and the amount of that item and returns the ascii value of the words as a decimal as the cost
    input -> str, float
    output ->float
    """
    global total_cost
    cost_numeric = 0.0
    for cost_item in item:
        cost_numeric += ord(cost_item) * 0.010
    cost_numeric*float(count)
    cost_total = str("%.2f" % cost_numeric)
    total_cost += cost_numeric
    return cost_total

def choice_add():
    """
    This function has no input or ouput and adds items to the shopping cart list either as a str or dict
    """
    add_cart = {}
    new_item = input('What would you like to buy?').lower()
    shopping_cart.append(new_item)
    item_count = input (f"How many {new_item} would you like?")#Junk collector
    while item_count.isdigit() == False:
        if item_count.isdigit() == False:
            item_count = ''
            print ("Please input the amount of items")
            item_count = input (f"How many {new_item} would you like?")
    add_cart.update({f'number of {new_item}': item_count})
    item_total = item_cost(new_item, item_count)
    add_cart.update({f'cost of {new_item}': item_total})
    shopping_cart.append(add_cart)


def choice_del():
    """
    This function has no input or output but deletes a str and a dictionary from the list based on input
    """
    global total_cost
    global shopping_cart
    rid_me = input("What item would you like to remove?").lower()
    while rid_me not in shopping_cart: #Junk collector   
        if rid_me not in shopping_cart:
            print("Please enter an item you have bought")
            rid_me = input("What item would you like to remove?").lower()
    if rid_me in shopping_cart:
        total_cost -= float(shopping_cart[shopping_cart.index(rid_me)+1].get(f'cost of {rid_me}'))
        shopping_cart = shopping_cart[:shopping_cart.index(rid_me)] + shopping_cart[shopping_cart.index(rid_me)+2:]

def print_out():
    """
    This function prints the user's purchases to the terminal
    """
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

    
user_attr()
print("Your Reciept")
print_out()

