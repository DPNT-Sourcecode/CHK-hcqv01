from collections import Counter


# noinspection PyUnusedLocal
prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

class InvalidCheckoutError(Exception):
    pass

def calculate_multi_reduction(sku, amount):
    """
        Calculates the discount for a given SKU and the amount of items
    """
    if sku == 'A':
        large_discount_amount = amount // 5
        small_discount_amount = (amount - (large_discount_amount * 5)) // 3
        return (large_discount_amount * 50) + (small_discount_amount * 20)

    if sku == 'B':
        multi_units = amount // 2
        return multi_units * 15

    return 0

def calculate_cost_of_sku(sku, amount):
    """
        Calculates the cost of an individual SKU
    """
    return prices[sku] * amount - calculate_multi_reduction(sku, amount)

def parse_skus(raw_string):
    """
        Parses the SKU string to extract the individual SKUs
    """
    no_delim = raw_string.replace(',', '').replace(' ', '')
    return list(no_delim)


def process_checkout(skus):
    if not isinstance(skus, str):
        raise InvalidCheckoutError

    if len(skus) == 0:
        return 0

    parsed_skus = parse_skus(skus)
    if len(parsed_skus) == 0 or any(sku not in prices.keys() for sku in parsed_skus):
        raise InvalidCheckoutError

    # calculate cost
    frequency_dict = Counter(parsed_skus)
    total_price = 0
    for key, value in frequency_dict.items():
        total_price += calculate_cost_of_sku(key, value)

    return total_price



# skus = unicode string
def checkout(skus):
    try:
        return process_checkout(skus)
    except InvalidCheckoutError:
        return -1






