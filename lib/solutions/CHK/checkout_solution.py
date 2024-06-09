import array
from collections import Counter
from copy import copy

"""
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 | a
| B    | 30    | 2B for 45              | a
| C    | 20    |                        | a
| D    | 15    |                        | a
| E    | 40    | 2E get one B free      | a
| F    | 10    | 2F get one F free      | a
| G    | 20    |                        | a
| H    | 10    | 5H for 45, 10H for 80  | a
| I    | 35    |                        | a
| J    | 60    |                        | a
| K    | 80    | 2K for 150             | a
| L    | 90    |                        | a
| M    | 15    |                        | a
| N    | 40    | 3N get one M free      | a
| O    | 10    |                        | a
| P    | 50    | 5P for 200             | a
| Q    | 30    | 3Q for 80              | a
| R    | 50    | 3R get one Q free      | a
| S    | 30    |                        | a
| T    | 20    |                        | a
| U    | 40    | 3U get one U free      | a
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        | a
| X    | 90    |                        | a
| Y    | 10    |                        | a
| Z    | 50    |                        | a
+------+-------+------------------------+
"""

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
              "amount": 3,
              "free_item": "U",
          }
      ]
    },
    # "V": 50,
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
    for sku in sku_copy:
        sku_options = prices[sku]

        if 'multi_discount' in sku_options:
            for discount in sku_options['multi_discount']:
                if discount['free_item'] == sku:
                    amount_of_sku = sku_copy[sku] or 0
                    if amount_of_sku >= 3 and amount_of_sku >= discount["amount"] + 1:
                        sku_copy[sku] = amount_of_sku - amount_of_sku // (discount['amount'] + 1)
                else:
                    amount_of_sku_reduction = (sku_copy[sku] or 0) // discount["amount"]
                    potential_new_balance = (sku_copy[discount["free_item"]] or 0) - amount_of_sku_reduction
                    sku_copy[discount["free_item"]] = potential_new_balance if potential_new_balance >= 0 else 0

    return sku_copy



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









