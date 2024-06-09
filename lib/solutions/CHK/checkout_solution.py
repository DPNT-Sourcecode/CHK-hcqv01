

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1
    individual_skus = [x.strip() for x in skus.split(',')]
    print(individual_skus)
    return 10


