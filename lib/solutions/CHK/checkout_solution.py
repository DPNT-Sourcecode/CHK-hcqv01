

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str) or len(skus) == 0:
        return -1

    individual_skus = [x.strip().upper() for x in skus.split(',')]

    if len(individual_skus) == 0:
        return -1


    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }

    total_price = 0
    for sku in individual_skus:
        item_price = prices[sku]
        total_price += item_price

    return total_price





