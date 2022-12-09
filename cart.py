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
    c_choice = user_resp
    while c_choice != 'quit':
        if c_choice == 'add':
            shopping_cart[input('Please add a food')] : hold_cart
            c_choice = input("What would you like to do in the store today?")
    return hold_cart
print(user_resp())
print(user_attr())