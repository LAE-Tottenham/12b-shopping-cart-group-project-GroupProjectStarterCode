from Currency import convert_money
from Food_functions import menutable
from Food_functions import shopping_cart_func
from Food_functions import checkout
import pprint
import json
from rich.console import Console
from rich.table import Table
import questionary
import pyfiglet 

console = Console()
def mainmenu():
    console.print("[u][i]Welcome to x restaurant[/i][/u]", style="bold red", justify="center")
    choice = questionary.select(
        "Choose an option: ",
        choices=[
            "Open the menu",
            "Currency Exchange",
            "Shopping Cart",
            "Checkout"
        ]).ask()
    if choice == "Open the menu":
        menutable()
        mainmenu()

            

    elif choice == "Currency Exchange":
        convert_money()
        mainmenu()
    
    elif choice == "Shopping Cart":
        shopping_cart_func()
        mainmenu()



    elif choice == "Checkout":
        checkout()
        mainmenu()
        
mainmenu()
