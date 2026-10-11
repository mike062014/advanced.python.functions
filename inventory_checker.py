try:
    items = ["pencil", "eraser", "notebook", "sharpener", "glue"]
    stock = [12, 0, 8, 5, 3]

    inventory = {item: count for item, count in zip(items, stock)}
    print("inventory stock:",inventory)

    items_stock = [item for item in items if inventory[item] > 0]
    print("items in stock",items_stock)

    wanted_item = input("what item do you want to buy? ")

    if wanted_item not in inventory or inventory[wanted_item] == 0:
        print("choosen items was out of stock, stopping...")
        exit()

    prices = [3, 4, 10, 5, 6]
    add_price = int(input("enter the additional prices to every item: "))

    extra_price = list(map(lambda p: p + add_price, prices))
    print("prices after addtion:",extra_price)

    item_index = items.index(wanted_item)
    wanted_prices = extra_price[item_index]
    print("price of",wanted_item, "after addition",wanted_prices)

    inventory[wanted_item] = inventory[wanted_item]
    print(wanted_item,"purchased, updating stock...",inventory[wanted_item])

    print("==============SCHOOL INVENTORY CHECKER===========================")
    print("item bought",wanted_item)
    print("price paid",wanted_prices)
    print("updated stock",inventory)
    print("=================================================================")
except ValueError:
    print("input the items listed!!")