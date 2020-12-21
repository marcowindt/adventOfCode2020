import os


TEST_FOODS = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""


def solution():
    # foods = TEST_FOODS
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        foods = fd.read()

    ingredients = set()
    ingredients_count = dict()
    allergens = dict()
    for food in foods.splitlines():
        parts = food.split(" (contains ")
        left = parts[0].split(" ")
        right = parts[1].split(")")[0].split(", ")
        ingredients = ingredients.union(set(left))

        for ing in set(left):
            if ing in ingredients_count:
                ingredients_count[ing] += 1
            else:
                ingredients_count[ing] = 1

        for allergen in right:
            if allergen not in allergens:
                allergens[allergen] = set(left)
            else:
                allergens[allergen] = allergens[allergen].intersection(set(left))

    not_terrible = ingredients.difference(set.union(*allergens.values()))
    # print(not_terrible)

    cnt = 0
    for ing in not_terrible:
        cnt += ingredients_count[ing]
    print("1:", cnt)

    for allergen in allergens:
        for ing in not_terrible:
            if ing in allergens[allergen]:
                allergens[allergen].remove(ing)
    # print(allergens)

    i = 0
    # big enough number
    while i < 100:
        for allergen in allergens:
            ing = allergens[allergen]
            if len(ing) == 1:
                for other_allergen in allergens:
                    if other_allergen != allergen:
                        allergens[other_allergen] = allergens[other_allergen].difference(allergens[allergen])
        i += 1

    # print(allergens)

    # inverted_allergens = dict()
    # for allergen in allergens:
    #     inverted_allergens[allergens[allergen].pop()] = allergen
    #
    # print(inverted_allergens)

    sorted_ingredients_by_allergen = []
    for allergen in sorted(allergens.keys()):
        sorted_ingredients_by_allergen.append(allergens[allergen].pop())

    canonical_dangerous_ingredients = ""
    for ing in sorted_ingredients_by_allergen:
        canonical_dangerous_ingredients += ing + ","
    print("2:", canonical_dangerous_ingredients[:-1])


if __name__ == '__main__':
    solution()
