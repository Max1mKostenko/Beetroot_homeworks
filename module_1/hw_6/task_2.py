stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

fruit = input(f'Please enter some fruit from this list {list(stock.keys())}: ').lower()

if fruit in stock:
    multiply = stock[fruit]
    total_price = sum(prices.values()) * multiply
    print(f"{sum(prices.values())} * {multiply} = {total_price}")
else:
    print("Please enter a valid type of fruit")
