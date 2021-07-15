import datetime
import re
from datetime import date

from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import FunctionItem, SubmenuItem

from barbecue import Barbecue
from bottom_freezer import BottomFreezer
from dining_chair import DiningChair
from dining_table import DiningTable
from four_k_uhd import FourKUHD
from laptop import Laptop
from loveseat import Loveseat
from macbook import Macbook
from microwave import Microwave
from payment_card import PaymentCard
from shopping_cart import ShoppingCart
from smart_tv import SmartTV
from sofa import Sofa
from top_freezer import TopFreezer

QUIT_CHAR = 'q'
CARDNUM_REGEX = r'^(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$'
EXPDATE_REGEX = r'^(0[1-9]|1[0-2])\/([0-9]{4})$'
EXPDATE_MONTH_REGEX = r'^(0[1-9]|1[0-2])(?=\/)'
EXPDATE_YEAR_REGEX = r'(?<=\/)([0-9]{4})$'
CARDHOLDER_REGEX = r'^((?:[A-Za-z]+ ?){1,3})$'
BALANCE_REGEX = r'[+-]?([0-9]*[.])?[0-9]+'


def select_products(products):
    for product in products:
        print(product)

    product_id = input('\nEnter product ID you would like to buy (or press q to quit): ')

    if product_id == QUIT_CHAR:
        return

    product_exists = False
    for product in products:
        if product.id == product_id:
            add_to_cart(product)
            product_exists = True
            break
    if not product_exists:
        print(f'Product with ID "{product_id}" does not exist')


def add_to_cart(product):
    quantity = input('Enter quantity (or press q to quit): ')
    if quantity == QUIT_CHAR:
        return
    cart.add(product, int(quantity))


def pay():
    if cart.empty():
        print("The shopping cart is empty, payment cancelled.")
    else:
        print(f"Cart amount: ${cart.amount}")
        while True:
            card_num = input("Input your card number without spaces (or press q to quit):")
            if card_num == QUIT_CHAR:
                return
            else:
                if re.match(CARDNUM_REGEX, card_num):
                    break
                else:
                    print('The card number is invalid.')

        while True:
            expiry_date = input("Input expiry date as mm/yyyy (or press q to quit):")
            if expiry_date == QUIT_CHAR:
                return
            else:
                if re.match(EXPDATE_REGEX, expiry_date):
                    card_date = datetime.datetime(int(re.findall(EXPDATE_YEAR_REGEX, expiry_date)[0]),
                                                  int(re.match(EXPDATE_MONTH_REGEX, expiry_date).group()), 1)
                    today_date = datetime.datetime(date.today().year, date.today().month, 1)
                    if card_date >= today_date:
                        break
                    else:
                        print('The card has expired.')
                else:
                    print('The expiry date is invalid.')

        while True:
            card_holder_name = input("Input card holder name (or press q to quit):")
            if card_holder_name == QUIT_CHAR:
                return
            else:
                if re.match(CARDHOLDER_REGEX, card_holder_name):
                    break
                else:
                    print('The card holder name is invalid.')

        while True:
            balance = input("Input card balance (or press q to quit):")
            if balance == QUIT_CHAR:
                return
            else:
                if re.match(BALANCE_REGEX, balance):
                    balance = float(balance)
                    break
                else:
                    print('The card balance is invalid.')

        card = PaymentCard(card_num, expiry_date, card_holder_name, balance)
        order_price = cart.amount
        if card.balance < order_price:
            print(f"PAYMENT DECLINED: Your balance is not enough for the payment ({order_price}/{card.balance})")
        else:
            card_balance_old = card.balance
            card.balance -= order_price
            print("\nPAYMENT SUCCESSFUL!")
            print(f"Old card balance: ${card_balance_old}")
            print(f"New card balance: ${card.balance}")
            print("\nReceipt:")
            cart.show()
            cart.clear()
            print("\nTHANK YOU!")


if __name__ == "__main__":
    # Initialize a catalogue of products
    sofas = [Sofa('001', 'Ikea', 'Sofari1', 150, 15, 'red', 320, 200),
             Sofa('002', 'Ikea', 'Sofari2', 160, 11, 'blue', 400, 250),
             Sofa('003', 'Ikea', 'Sofari3', 170, 13, 'white', 310, 210)]
    loveseats = [Loveseat('011', 'Ikea', 'Seaty1', 50, 12),
                 Loveseat('012', 'Ikea', 'Seaty2', 45, 11)]
    dining_tables = [DiningTable('021', 'Ikea', 'Table1', 200, 12, 'France', 'Wood'),
                     DiningTable('022', 'Ikea', 'Table2', 115, 15, 'France', 'Plastic')]
    dining_chairs = [DiningChair('031', 'Ikea', 'Chair1', 35, 13),
                     DiningChair('032', 'Ikea', 'Chair2', 40, 15),
                     DiningChair('033', 'Ikea', 'Chair3', 30, 18)]
    bottom_freezers = [BottomFreezer('041', 'Samsung', 'Ice1', 500, 12, 3, 'White', 0.20),
                       BottomFreezer('042', 'Philips', 'Ice2', 515, 15, 2, 'Black', 0.25)]
    top_freezers = [TopFreezer('051', 'Samsung', 'Ice1', 450, 16, 3, 'White', 0.30),
                    TopFreezer('052', 'Philips', 'Ice2', 300, 15, 4, 'Black', 0.20),
                    TopFreezer('053', 'Philips', 'Ice3', 315, 18, 2, 'Metal', 0.25)]
    barbecues = [Barbecue('061', 'AMD', 'KDL15', 240, 0)]
    microwaves = [Microwave('071', 'Samsung', 'Wave1', 500, 11, 50),
                  Microwave('072', 'Panasonic', 'Wave2', 550, 16, 40)]
    smart_tv = [SmartTV('081', 'LG', 'Smart1', 1000, 11, 'yes', 'yes', 3),
                SmartTV('082', 'HP', 'Smart2', 950, 12, 'yes', 'yes', 2),
                SmartTV('083', 'HP', 'Smart3', 1200, 13, 'no', 'yes', 3)]
    four_k_uhd = [FourKUHD('091', 'Delco', 'UltraHD', 1500, 16, 'yes', 'yes', 2),
                  FourKUHD('092', 'JVC', 'MegaHD', 2000, 11, 'no', 'yes', 2)]
    laptops = [Laptop('101', 'Lenovo', 'LNV-14', 1950, 11, 'yes', 'yes', 1, 4),
               Laptop('102', 'HP', 'HP-6', 2100, 16, 'yes', 'yes', 2, 8),
               Laptop('103', 'Acer', 'AC-55', 2500, 13, 'yes', 'yes', 1, 16)]
    macbooks = [Macbook('111', 'Apple', 'Air1', 2500, 11, 'yes', 'yes', 1, 4),
                Macbook('112', 'Apple', 'Air2', 2900, 12, 'yes', 'yes', 1, 8)]

    # Initialize shopping cart
    cart = ShoppingCart()

    # Create menu
    print('Welcome to ABC store!')

    ## Furniture

    ### Furniture -> Living room
    living_room_menu = SelectionMenu([], 'Living Room')
    display_sofas_item = FunctionItem("Sofas", select_products, [sofas])
    display_loveseats_item = FunctionItem("Loveseats", select_products, [loveseats])
    living_room_menu.append_item(display_sofas_item)
    living_room_menu.append_item(display_loveseats_item)

    ### Furniture -> Dining room
    display_tables_item = FunctionItem("Dining Tables", select_products, [dining_tables])
    display_chairs_item = FunctionItem("Dining Chairs", select_products, [dining_chairs])
    dining_room_menu = SelectionMenu([], 'Dining Room')
    dining_room_menu.append_item(display_tables_item)
    dining_room_menu.append_item(display_chairs_item)

    furniture_menu = SelectionMenu([], 'Furniture')
    furniture_menu.append_item(SubmenuItem("Living Room", living_room_menu, furniture_menu))
    furniture_menu.append_item(SubmenuItem("Dining Room", dining_room_menu, furniture_menu))

    ## Appliance

    ### Appliance -> Refrigerator
    display_bottom_freezer_item = FunctionItem("Bottom Freezers", select_products, [bottom_freezers])
    display_top_freezer_item = FunctionItem("Top Freezer", select_products, [top_freezers])
    refrigerator_menu = SelectionMenu([])
    refrigerator_menu.append_item(display_bottom_freezer_item)
    refrigerator_menu.append_item(display_top_freezer_item)

    ### Appliance -> Cooking
    display_barbecues_item = FunctionItem("Barbecues", select_products, [barbecues])
    display_microwaves_item = FunctionItem("Microwaves", select_products, [microwaves])
    cooking_menu = SelectionMenu([])
    cooking_menu.append_item(display_barbecues_item)
    cooking_menu.append_item(display_microwaves_item)

    appliance_menu = SelectionMenu([], 'Appliance')
    appliance_menu.append_item(SubmenuItem("Refrigerator", refrigerator_menu, appliance_menu))
    appliance_menu.append_item(SubmenuItem("Cooking", cooking_menu, appliance_menu))

    ## Electronics

    ### Electronics -> Television
    display_smart_tv_item = FunctionItem("Smart TV", select_products, [smart_tv])
    display_four_k_uhd_item = FunctionItem("4K UHD", select_products, [four_k_uhd])
    television_menu = SelectionMenu([])
    television_menu.append_item(display_smart_tv_item)
    television_menu.append_item(display_four_k_uhd_item)

    ### Electronics -> Computer
    display_laptops_item = FunctionItem("Laptops", select_products, [laptops])
    display_macbooks_item = FunctionItem("Macbooks", select_products, [macbooks])
    computer_menu = SelectionMenu([])
    computer_menu.append_item(display_laptops_item)
    computer_menu.append_item(display_macbooks_item)

    electronics_menu = SelectionMenu([], 'Electronics')
    electronics_menu.append_item(SubmenuItem("Television", television_menu, electronics_menu))
    electronics_menu.append_item(SubmenuItem("Computers", computer_menu, electronics_menu))

    # Main menu and catalogue
    menu = ConsoleMenu("ABC Store", "Home Menu")
    catalogue_menu = SelectionMenu([], 'Catalogue')
    catalogue_menu.append_item(SubmenuItem("Furniture", furniture_menu, catalogue_menu))
    catalogue_menu.append_item(SubmenuItem("Appliance", appliance_menu, catalogue_menu))
    catalogue_menu.append_item(SubmenuItem("Electronics", electronics_menu, catalogue_menu))
    catalogue_item = SubmenuItem("Catalogue", catalogue_menu, menu)
    menu.append_item(catalogue_item)

    # Add a fixed set of actions to all menus
    default_actions = [FunctionItem("Show Shopping Cart", cart.show, []),
                       FunctionItem("Pay", pay, [])]
    menus = [menu, catalogue_menu,
             furniture_menu, living_room_menu, dining_room_menu,
             appliance_menu, refrigerator_menu, cooking_menu,
             electronics_menu, television_menu, computer_menu]
    for cur_menu in menus:
        for action in default_actions:
            cur_menu.append_item(action)

    menu.show()
