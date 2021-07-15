# E-commerce ABC store

### About 
This project aims to implement an e-commerce platform

### Prerequisites
Before running this project, you should install and import the library https://pypi.org/project/console-menu/:
```bash
$ pip install console-menu
```

### Catalogue hierarchy description
The ABC store has a product catalogue, which is organized into products categories: Furniture, Appliance and Electronics. 
Each category has a sub-category, and each sub-category has products.
   
**Furniture** category has 2 sub-categories: _Living room_, _Dining room_. 

_Living room_ products are: Sofas, loveseats.

_Dining room_ products are: Dining tables, Dinning chairs.
   
**Appliance** category has 2 sub-categories: Refrigerators, Cooking.

_Refrigerators_ products are: Bottom freezers, Top freezers.

_Cooking_ products are: Barbecues, Microwaves.

**Electronics** category has 2 sub-categories: Television, Computers.

_Television_ products are: Smart TV, 4K UHD.

_Computer_ products are: Laptops, Macbooks.

### Product description
Each product has a brand, a type (this attribute will refer a sub-category, ex. Living room, Computers, etc),
a display name, a price, an inventory (number of items), and an inventory status 
(that tells if the product is in stock, low stock or out of stock).

Warranty: 2 years for furniture, 3 years for appliances, and 1 year for electronics.

Sofa should also have these additional attributes: color, Height and width.

Dining tables should also have these additional attributes: made in (ex. Europe), material (ex. wood).

Refrigerators should have these additional attributes: drawers (ex. value: 3), door color, freezer capacity (ex. 0,25 m3).

Microwaves should have these additional attributes: depth (ex. 39 cm).

Television should have these additional attributes: Bluetooth (yes/no as values) WI-FI (yes/no as values), 
HDMI input (ex. 3).

Computers should have these additional attributes: Bluetooth (yes/no as values) WI-FI (yes/no as values), 
HDMI output (ex. 1) RAM size (ex. 8 GB).

### Shopping Cart
When a user selects a product and its quantity, it is added to the user's shopping cart.

At any time, the user can display the content of its shopping cart.
There he will see the added products, its quantity and the final price.

Example: 
```
Product Price Quantity Total
Sofari1 $150    2       $300
Sofari3 $170    1       $170
----------------------------
Total amount:           $470
```

### Payment by Credit Card
Regex was used to check if the card number, cardholder's name, card balance were entered correctly, 
and that the card expiry date is valid.

At any time, the user can pay for the selected product.

When a customer chooses a payment option, he must enter his card details.

Example:

* Input your card number (without spaces): 2536264515632548
* Input expiry date (mm/yyyy): 02/2025
* Input card holder name: Bob Smith
* Input card balance: 1000

If there was an error when entering data, the client is asked to re-enter it. 

If all the data is entered successfully, the payment proceeds according to the following example:
 
```
Pay successful!
Old card balance: $1000.0
New card balance: $180.0

Receipt:

Product     Price   Quantity    Total
Sofari2     $160        3       $480
Sofari3     $170        2       $340
-------------------------------------
Total amount:                   $820

THANK YOU!
```
When a user buys a product, this product’s inventory will decrease.

If product inventory is >10, its inventory status is ‘in stock’, if <10 is ‘lo w stock’, if =0 is 'out of stock'.

The exception is the Furniture category. As soon as the inventory in the Furniture category falls below 5,
the inventory of this product is increased by calling a method. It is assumed that these products are made in France, 
so they are quickly delivered to the store.

### Additional features
When the user is asked to enter data (ex. product ID, card number), there is an option to cancel the command and 
go one step back, this is done by pressing the 'q' button.

Getter and setter methods are used in ProductBasicAttributes class to work with warranty and inventory status properties.