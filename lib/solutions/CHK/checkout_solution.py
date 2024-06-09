from collections import Counter


# noinspection PyUnusedLocal
prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

def calculate_multi_reduction(sku, amount):
    if sku == 'A':
        multi_units = amount // 3
        return multi_units * 20

    if sku == 'B':
        multi_units = amount // 2
        return multi_units * 15

    return 0

def calculate_cost_of_sku(sku, amount):
    return prices[sku] * amount - calculate_multi_reduction(sku, amount)

def parse_skus(raw_string):
    no_delim = raw_string.replace(',', '')
    return [x.strip().upper() for x in no_delim]

# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str) or len(skus) == 0:
        return -1

    parsed_skus = parse_skus(skus)
    if len(parsed_skus) == 0:
        return -1

    frequency_dict = Counter(parsed_skus)
    total_price = 0
    for key, value in frequency_dict.items():
        total_price += calculate_cost_of_sku(key, value)

    return total_price









