
product = [
('p01', 'T-shirt', 19.99),
    ('p02', 'Jean', 39.99),
    ('p03', 'Chaussures', 59.99),
    ('p04', 'Casquette', 14.99)
]

product_id = {
'p01': 50,
    'p02': 30,
    'p03': 20,
    'p04': 10
}
product_to_sell = "p01"

for pid,name,price in product:
    if pid == product_to_sell:
        print(f"le nom est:{name} et son prix est de {price}")

stock_levels = product_to_sell -1
 print(f'la nouvelle valeur est de product est:')

