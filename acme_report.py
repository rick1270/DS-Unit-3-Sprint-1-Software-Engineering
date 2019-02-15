from acme import Product
from numpy import random

def generate_products(num = 30):
    ADJECTIVES = ['Awesome', 'Shiny', 'Impressive','Portable', 'Improved']
    NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    
    inventory =[]
    for i in range(num):
        ran_name = name1[random.randint(0,len(name1))]+" "+name2[random.randint(0,len(name2))]
        ran_price = random.randint(5,100)
        ran_weight = random.randint(5,100)
        ran_flam = random.randint(0,25)/10
        prod = Product(name=ran_name, price=ran_price, weight=ran_weight,
                       flammability=ran_flam)

        inventory.append(prod)
        return inventory
    
def inventory_report(inventory):
    from statistics import mean

    n_unique = len(set([x.name for x in inventory]))
    mean_price = mean([x.price for x in inventory])
    mean_weight = mean([x.weight for x in inventory])
    mean_flammability = mean([x.flammability for x in inventory])

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {n_unique}')
    print(f'Average price: {mean_price}')
    print(f'Average weight: {mean_weight}')
    print(f'Average flammability: {mean_flammability}')


if __name__ == '__main__':
    inventory_report(generate_products())
