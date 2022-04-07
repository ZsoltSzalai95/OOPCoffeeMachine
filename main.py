from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu=Menu()
coffee_maker=CoffeeMaker()
payment=MoneyMachine()

should_continue=True

def game():
  while should_continue:
    options=menu.get_items()
    order_name=input(f"What would you like? ({options}): \nTo turn off the machine just press the 'off' button! ").strip().lower()
  
    if order_name=="off":
      return
    elif order_name=="report":
      coffee_maker.report()
      payment.report()
    else:
      drink=menu.find_drink(order_name)  
      if coffee_maker.is_resource_sufficient(drink) and payment.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
game()
