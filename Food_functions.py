import pprint
import pyfiglet
from rich.console import Console
from rich.table import Table
from currency_converter import CurrencyConverter
from Currency import converter
c = CurrencyConverter()
shopping_cart = []
total_price = 0
console = Console()
def menutable():
    Food = {
        'Nasi Lemak': converter(3.00),
        'Nasi Goreng': converter(3.50),
        'Roti Chanai':  converter(2.50),
        'Pani Puri': converter(2.25),
        'Curly Fries': converter(1.50),
        'Biryani': converter(4.00),
        'Satay Chicken': converter(3.50),
        'Chicken Tikka Masala': converter(4.50),
        'Lamb Ribs': converter(5.00),
        'Fries': converter(1.25),
        }

    Drinks = {
        'Prime': converter(2.00),
        'Water': converter(0.50),
        'Sparkling Water': converter(1.00),
        'Milkshake': converter(2.00),
        "Chai": converter(1.00),
        'Lemonade': converter(1.50),
        'Coca Cola': converter(1.00),
        'Jasmine Tea': converter(0.80),
        'Bubble Tea': converter(2.00),
        'Mojito': converter(1.50), 
    }     
    
    
    result = pyfiglet.figlet_format("MENU")
    console.print(result, style="bold red", justify="center")


    # TABLE CONFIG

    table = Table(show_header=True,show_edge=True,show_lines=False, header_style="bold red")
    table.add_column("Meals", width=20)
    table.add_column("Price", width=12, justify="right")
    table.add_column("Drinks", width=20)
    table.add_column("Price", width=12, justify="right")

    # ROWS

    table.add_row(
        "Nasi Lemak", str(converter(3.00) + '0'), "Water", str(converter(0.50)+ '0')
    )
    table.add_row(
        "Nasi Goreng", str(converter(3.50)+ '0'), "Prime", str(converter(2.00) + '0')
    )
    table.add_row(
        "Roti Chanai", str(converter(2.50)+ '0'), "Sparkling Water", str(converter(1.00) + '0')
    )
    table.add_row(
        "Pani Puri", str(converter(2.25)), "Milkshake", str(converter(2.00)+ '0')
    )
    table.add_row(
        "Biryani", str(converter(4.00)+ '0'), "Chai", str(converter(1.00)+ '0')
    )
    table.add_row(
        "Satay Chicken", str(converter(3.50)+ '0'), "Lemonade", str(converter(1.50)+ '0')
    )
    table.add_row(
        "Chicken Tikka Masala", str(converter(4.50)+ '0'), "Coca Cola", str(converter(1.00)+ '0')
    )
    table.add_row(
        "Lamb Ribs", str(converter(5.00)+ '0'), "Jasmine Tea", str(converter(0.80)+ '0')
    )
    table.add_row(
        "Fries", str(converter(1.25)), "Bubble Tea", str(converter(2.00)+ '0')
    )
    table.add_row(
        "Curly Fries", str(converter(1.50)+ '0'), "Mojito", str(converter(2.50)+ '0')
    )
    
    console.print(table, justify="center")

    item_prices = []
    global total_price
    global shopping_cart
    print("What would you like to buy: ")
    print("Type # when finished")

    shop = True

    while shop:
        item = input()
        for x in item_prices:
            raw_price = float(x[1:])
            total_price += raw_price

        if item == "#":
            print("Items added to Shopping Cart: ")
            print(shopping_cart)
            print (f"Total: {total_price}")
            break
        
        
        if item in Food:
            shopping_cart.append(item)
            item_prices.append(Food[item])
        elif item in Drinks:
            shopping_cart.append(item)
            item_prices.append(Drinks[item])
        else:
            print(f"Sorry, but we don't have {item} on our menu. Would you like to order something else?")




            



def shopping_cart_func():
    global shopping_cart
    if shopping_cart == []:
        pprint.pprint("There are no items in your shopping cart. Please order an item.")
    else:
        pprint.pprint("Here are the items in your shopping cart: ")
        pprint.pprint(shopping_cart)


def checkout():
    global total_price
    if shopping_cart == []:
        print("You have no items added to your shopping cart.")
        return ""
    else:
        print(f"Would you like to purchase {shopping_cart} for {total_price}? (Y/N)")
        if input().lower() == "n":
            return "Please take your time!"
    
    
    
    print("PLEASE ENTER YOUR")
    
    
    card_num = input("Card number: ")
    
    if len(card_num) < 16 or len(card_num) > 19:
        print("Your number is too short.")
        card_num = input("Card number: ")
    for x in card_num:
        if x.isalpha():
            print("Your card number cannot have letters.")
            card_num = input("Card number: ")
    

    name = input("Full name: ")


    exp_date = input("Expiry date: ")
    if exp_date[:1].isdigit() == False or exp_date[3:].isdigit() == False:
        print("Your expiry date cannoy include letters.")
        exp_date = input("Expiry date: ")

    loc = input("PostCode: ")
    locprice = (int(total_price) * 2.5)
    print("Your total price including delivering fees is " +str(locprice) )
    print("Confirm? (Y/N)")
    if input().lower() == "y":
      print("Thank you")
    else:
        return
