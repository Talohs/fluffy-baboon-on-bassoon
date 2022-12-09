import json

def shop():
    cart = []
    valid_selections = ['a', 'r', 's', 'c']
    while True:
        selection = input('What would you like to do? \'a\' to add, \'r\' to remove, \'s\' to show, and \'c\' to checkout.')
        if selection not in valid_selections:
            print(f'Your selection \'{selection}\' is not a valid option.\nValid options are \'a\' to add, \'r\' to remove, \'s\' to show, and \'c\' to checkout.')
        else:
            if selection.lower() == 'a':
                item_to_add = input('What would you like to add to your shopping cart?').lower()
                cart.append(item_to_add)
            elif selection.lower() == 'r':
                item_to_remove = input(f'What would you like to remove? Your cart currently contains: {cart}').lower()
                confirm = input(f'Are you sure you want to remove {item_to_remove.title()} from your cart? \'y\' to confirm, any other key to cancel.')
                if confirm == 'y':
                    cart.remove(item_to_remove)
            elif selection.lower() == 's':
                print('Here are the current contents of your cart:')
                for i in cart:
                    print(i)
            else:
                output_dict = {}
                item_number = 1
                print('Thanks for shopping with us!')
                print('Here are the final contents of your cart.')
                for i in cart:
                    print(i)
                    output_dict[item_number] = i
                    item_number += 1
                print(f'Printing your receipt as receipt.json: {output_dict}')

                with open('receipt.json', 'w') as fp:
                    json.dump(output_dict, fp, indent=4)
                break

shop()