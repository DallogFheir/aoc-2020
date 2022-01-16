import re
from copy import deepcopy

def parse_foods(fh):
    foods_lst = []
    ingredient_set = set()
    food_regex = re.compile(r"(.*?) \(contains (.*?)\)")

    for line in fh:
        ingredient_str, allergen_str = re.match(food_regex, line).groups()

        ingredients = ingredient_str.split()
        allergens = allergen_str.split(", ")

        foods_lst.append((ingredients,allergens))
        ingredient_set |= set(ingredients)

    return foods_lst, ingredient_set

def map_allergens_to_ingredients(foods_lst):
    allergen_dict = {}

    for food in foods_lst:
        ingredients, allergens = food

        for allergen in allergens:
            if allergen in allergen_dict:
                allergen_dict[allergen] &= set(ingredients)
            else:
                allergen_dict[allergen] = set(ingredients)

    return allergen_dict

def check_if_ingredient_has_no_allergens(allergen_dict,ingredient):
    for possible_ingredients in allergen_dict.values():
        if ingredient in possible_ingredients:
            return False

    return True

def find_ingredients_without_allergens(allergen_dict,ingredient_set):
    ingredients_without_allergens = set()

    for ingredient in ingredient_set:
        if check_if_ingredient_has_no_allergens(allergen_dict,ingredient):
            ingredients_without_allergens.add(ingredient)

    return ingredients_without_allergens

def count_ingredients(food_lst,ingredient_set):
    count = 0

    for food in food_lst:
        ings, _ = food

        for ing in ingredient_set:
            count += ing in ings

    return count

def determine_allergens(allergen_dict):
    allergens = {}

    while allergen_dict:
        dict_copy = deepcopy(allergen_dict)

        for ing, alrgs in dict_copy.items():
            # take out the ingredient if there's only one allergen
            if len(alrgs) == 1:
                allergens[tuple(alrgs)[0]] = ing
                del allergen_dict[ing]
            else:
                new_alrgs = alrgs - set(allergens.keys())

                allergen_dict[ing] = new_alrgs

    return allergens

def make_canonical_ingredient_list(allergen_map):
    sorted_ings = sorted(allergen_map.keys(), key=lambda k: allergen_map[k])

    return ",".join(sorted_ings)
