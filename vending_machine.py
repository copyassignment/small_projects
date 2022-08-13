items_in_stock = [
    {
        "item_id": 0,
        "item_name": "Milky Bar",
        'item_price': 60,
    },
    {
        "item_id": 1,
        "item_name": "Fanta",
        'item_price': 90,
    },
    {
        "item_id": 2,
        "item_name": "Kurkure",
        'item_price': 25,
    },
    {
        "item_id": 3,
        "item_name": "Thumbs Up",
        'item_price': 90,
    },
    {
        "item_id": 4,
        "item_name": "Wai-Wai",
        'item_price': 20,
    },
]


the_item = []

reciept = """
\t\tPRODUCT -- PRICE
"""

sum = 0

run = True

print("----------The Items In Stock Are----------\n\n")

for i in items_in_stock:
    print(f"Item: {i['item_name']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")


def machine(items_in_stock, run, the_item):
    while run:

        buy_item = int(input("\n\nEnter the item code of the product you want to buy: "))

        if buy_item < len(items_in_stock):
            the_item.append(items_in_stock[buy_item])
        else:
            print("THE PRODUCT ID IS WRONG!")

        more_items = str(input("press any key to add more items and press q to quit.. "))

        if more_items == "q":
            run = False

    rec_bool = int(input(("1. print the reciept? 2. only print the total sum .. ")))
    if rec_bool == 1:
        print(create_reciept(the_item, reciept))
    elif rec_bool == 2:
        print(sum(the_item))
    else:
        print("INVALID ENTRY")


def sum(the_item):
    sum = 0

    for i in the_item:
        sum += i["item_price"]

    return sum

def create_reciept(the_item, reciept):

    for i in the_item:
        reciept += f"""
        \t{i["item_name"]} -- {i['item_price']}
        """

    reciept += f"""
        \tTotal --- {sum(the_item)}
        
        
        """
    return reciept


if __name__ == "__main__":
    machine(items_in_stock, run, the_item)
