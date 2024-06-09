

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1
    individual_skus = [x.strip() for x in skus.split(',')]

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }

    total_price = 0
    for sku in skus:
        print(sku)
        total_price += prices[sku]

    return total_price






