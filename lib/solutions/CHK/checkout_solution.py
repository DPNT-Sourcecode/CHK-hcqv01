import array
from collections import Counter
from copy import copy

# noinspection PyUnusedLocal
prices = {
    "A": {
      "base_cost": 50,
      "volume_discount": [
          {
              "amount": 3,
              "discount": 20,
          },
          {
              "amount": 5,
              "discount": 50
          }
      ]
    },
    "B": {
      "base_cost": 30,
      "volume_discount": [
          {
              "amount": 2,
              "discount": 15,
          }
      ]
    },
    "C": {
      "base_cost": 20,
    },
    "D": {
      "base_cost": 15,
    },
    "E": {
      "base_cost": 40,
      "multi_discount": [
          {
              "amount": 2,
              "free_item": "B",
          }
      ]
    },
    "F": {
      "base_cost": 10,
      "multi_discount": [
          {
              "amount": 2,
              "free_item": "F",
          }
      ]
    },
    "G": {
      "base_cost": 20,
    },
    "H": {
        "base_cost": 10,
        "volume_discount": [
            {
                "amount": 5,
                "discount": 5,
            },
            {
                "amount": 10,
                "discount": 20
            }
        ]
    },
    "I": {
      "base_cost": 35,
    },
    "J": {
      "base_cost": 60,
    },
    "K": {
      "base_cost": 80,
      "volume_discount": [
          {
              "amount": 2,
              "discount": 10,
          }
      ]
    },
    "L": {
      "base_cost": 90,
    },
    "M": {
      "base_cost": 15,
    },
    "N": {
      "base_cost": 40,
      "multi_discount": [
          {
              "amount": 3,
              "free_item": "M",
          }
      ]
    },
    "O": {
      "base_cost": 10,
    },
    "P": {
      "base_cost": 50,
      "volume_discount": [
          {
              "amount": 5,
              "discount": 50,
          }
      ]
    },
    "Q": {
      "base_cost": 30,
      "volume_discount": [
          {
              "amount": 3,
              "discount": 10,
          }
      ]
    },
    "R": {
      "base_cost": 50,
      "multi_discount": [
          {
              "amount": 3,
              "free_item": "Q",
          }
      ]
    },
    "S": {
      "base_cost": 30,
    },
    "T": {
      "base_cost": 20,
    },
    "U": {
      "base_cost": 40,
      "multi_discount": [
          {
              "amount": 4,
              "free_item": "U",
          }
      ]
    },
    "V": {
      "base_cost": 50,
      "volume_discount": [
          {
              "amount": 2,
              "discount": 10,
          },
          {
              "amount": 3,
              "discount": 20
          }
      ]
    },
    "W": {
      "base_cost": 20,
    },
    "X": {
      "base_cost": 90,
    },
    "Y": {
      "base_cost": 10,
    },
    "Z": {
      "base_cost": 50,
    },
}

range_discounts = [
    {
        "range": ["S", "T", "X", "Y", "Z"],
        "amount_required": 3,
        "base_cost": 45,
    }
]

class InvalidCheckoutError(Exception):
    pass

def calculate_cost_of_sku(sku, amount):
    """
        Calculates the cost of an individual SKU
    """
    volume_discount = calculate_volume_discount(sku, amount)
    return prices[sku]["base_cost"] * amount - volume_discount

def calculate_volume_discount(sku, volume):
    """
        Calculates the volume discount for a given SKU and the amount of items
    """
    sku_options = prices[sku]
    total_discount = 0

    if 'volume_discount' in sku_options:
        un_ordered_discounts = sku_options['volume_discount']
        ordered_discounts = sorted(un_ordered_discounts, key=lambda x: x['amount'], reverse=True)

        affected_units = 0
        for discount in ordered_discounts:
            discount_amount = (volume - affected_units) // discount['amount']
            affected_units += discount_amount * discount['amount']
            total_discount += discount_amount * discount['discount']

    return total_discount


def calculate_free_discount_deductions(skus: array) -> array:
    """
    Calculates the free discount for skus
    """
    sku_copy = copy(skus)
    for sku in skus:
        sku_options = prices[sku]

        if 'multi_discount' in sku_options:
            for discount in sku_options['multi_discount']:
                if discount['free_item'] == sku:
                    amount_of_sku = sku_copy[sku] or 0
                    if amount_of_sku >= 3:
                        groups_of_number = amount_of_sku // discount['amount']
                        groups_of_removal = groups_of_number // discount['amount']
                        print(sku + " " + str(groups_of_removal))
                        final_amount = (amount_of_sku // discount['amount']) - groups_of_removal
                        print(sku + " " + str(final_amount))
                        sku_copy[sku] = amount_of_sku - final_amount
                else:
                    amount_of_sku_reduction = (sku_copy[sku] or 0) // discount["amount"]
                    potential_new_balance = (sku_copy[discount["free_item"]] or 0) - amount_of_sku_reduction
                    sku_copy[discount["free_item"]] = potential_new_balance if potential_new_balance >= 0 else 0

    return sku_copy

def calculate_range_discount(sku_frequency):
    """
        Calculates range discounts and removes them from the total SKUs
    """
    grouping = 3
    accepted_items = ["S", "T", "X", "Y", "Z"]
    flat_sku = []
    for key, value in sku_frequency.items():
        for i in range(value):
            flat_sku.append(key)


    print(flat_sku)

    found_pairs = 0

    loop = True
    while loop:
        print('- loop')

        letters = []

        for i in range(grouping):
            print("-- looking for letter " + str(i))

            for letter in flat_sku:
                if letter in accepted_items:
                    print("-- got one " + letter)
                    letters.append(letter)
                    break



        print("-- found " + str(len(letters)))


        if len(letters) == grouping:
            found_pairs += 1
            for letter in letters:
                flat_sku.pop(flat_sku.index(letter))
        else:
            loop = False

    print(found_pairs)
    print(flat_sku)

    return Counter(flat_sku), found_pairs * 45


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
    frequency_dict, range_total_cost =  calculate_range_discount(frequency_dict)

    total_price = 0
    for key, value in frequency_dict.items():
        total_price += calculate_cost_of_sku(key, value)

    return total_price + range_total_cost



# skus = unicode string
def checkout(skus):
    try:
        return process_checkout(skus)
    except InvalidCheckoutError:
        return -1



