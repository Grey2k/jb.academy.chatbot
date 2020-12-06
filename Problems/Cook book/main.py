pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input().strip()

dishes = []

if ingredient in pasta.split(', '):
    dishes.append('pasta')

if ingredient in apple_pie.split(', '):
    dishes.append('apple pie')

if ingredient in ratatouille.split(', '):
    dishes.append('ratatouille')

if ingredient in chocolate_cake.split(', '):
    dishes.append('chocolate cake')

if ingredient in omelette.split(', '):
    dishes.append('omelette')

for dish in dishes:
    print("{} time!".format(dish))
