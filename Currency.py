from currency_converter import CurrencyConverter
import pprint
from currencies import Currency
c = CurrencyConverter()
current = 'GBP'
exchange_rates = {
    'USD' : 1.31,
    'EUR' : 1.19,
    'CAD' : 1.80,
    'MYR' : 5.60,
    'JPY' : 194.69,
    'GBP' : 1.00
        }


def convert_money():
    global current
    pprint.pprint(exchange_rates)
    new_currency = input("Enter your desired currency:")
    if new_currency.upper() in exchange_rates:
        current = new_currency
        print(f"Currency updated to: {current}")
    else:
        print("Invalid currency. Please select a valid option.")  
    return current.upper()




def converter(price):
    global current
    currency = Currency(current.upper())
    price = currency.get_money_format(round(c.convert(price, 'GBP', current.upper()), 2))
    return price



