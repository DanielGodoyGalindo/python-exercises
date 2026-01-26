"""
Traveling Shopper
Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
Each array item you want to purchase will be in the same format.
Use the following exchange rates to convert values:

Currency	1 Unit Equals
USD	        1.00 USD
EUR	        1.10 USD
GBP	        1.25 USD
JPY	        0.0070 USD
CAD	        0.75 USD
If you can afford all the items in the list, return "Buy them all!".
Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given.

1. buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]) should return "Buy the first 2 items.".
2. buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]) should return "Buy them all!".
3. buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]) should return "Buy the first 3 items.".
"""

currency_equals = {"USD": 1.00, "EUR": 1.10, "GBP": 1.25, "JPY": 0.0070, "CAD": 0.75}


def to_usd(amount, currency):
    return float(amount) * currency_equals[currency]


def buy_items(funds, items: list):
    # change funds to USD
    money_left = to_usd(funds[0], funds[1])
    # change items to USD
    usd_items = []
    for price, currency in items:
        usd_price = to_usd(price, currency)
        usd_items.append([usd_price, "USD"])
    # check affordable items
    items_to_buy = 0
    for item in usd_items:
        if float(item[0]) <= money_left:
            items_to_buy += 1
            money_left -= item[0]
        else:
            break
    if items_to_buy == len(items):
        return "Buy them all!"
    return f"Buy the first {items_to_buy} items."


print(
    buy_items(
        ["100.00", "CAD"],
        [
            ["20.00", "USD"],
            ["15.00", "EUR"],
            ["10.00", "GBP"],
            ["6000", "JPY"],
            ["5.00", "CAD"],
            ["10.00", "USD"],
        ],
    )
)
