import array
from collections import Counter


# noinspection PyUnusedLocal
prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
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

def calculate_free_discount_deductions(skus: array) -> array:
    """
    Calculates the free discount for skus
    """
    amount_of_e_sku_discounts = (skus["E"] or 0) // 2
    if "B" in skus.keys():
        potential_new_b_balance = skus["B"] - amount_of_e_sku_discounts
        new_b_balance = potential_new_b_balance if potential_new_b_balance >= 0 else 0
        skus["B"] = new_b_balance

    amount_of_f_sku = skus["F"] or 0
    discount_f_amount = amount_of_f_sku
    if discount_f_amount >= 3:
        while discount_f_amount >= 2:
            discount_f_amount -= discount_f_amount // 2
        print(discount_f_amount)
        skus["F"] = amount_of_f_sku - discount_f_amount

    return skus



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
    frequency_dict = calculate_free_discount_deductions(frequency_dict)
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






