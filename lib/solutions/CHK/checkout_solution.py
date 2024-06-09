from collections import Counter


# noinspection PyUnusedLocal
def calculate_cost_of_sku(sku, amount):
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }

    return prices[sku] * amount


# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str) or len(skus) == 0:
        return -1

    parsed_skus = [x.strip().upper() for x in skus.split(',')]
    if len(parsed_skus) == 0:
        return -1

    frequency_dict = Counter(parsed_skus)
    total_price = 0
    for key, value in frequency_dict.items():
        total_price += calculate_cost_of_sku(key, value)

    return total_price






