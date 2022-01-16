import allergens

with open("test_input.txt") as f:
    food_lst, ing_set = allergens.parse_foods(f)
alrg_dict = allergens.map_allergens_to_ingredients(food_lst)

# ingredients without allergens
ings_wo_alrgs = allergens.find_ingredients_without_allergens(alrg_dict, ing_set)
count = allergens.count_ingredients(food_lst,ings_wo_alrgs)

assert ings_wo_alrgs=={"kfcds", "nhms", "sbzzf", "trh"}
assert count==5

# map ingredients to allergens
allergen_map = allergens.determine_allergens(alrg_dict)

assert allergen_map=={
    "mxmxvkd" : "dairy",
    "sqjhc" : "fish",
    "fvjkl" : "soy"
}

# canonical ingredient list
canonical_lst = allergens.make_canonical_ingredient_list(allergen_map)

assert canonical_lst=="mxmxvkd,sqjhc,fvjkl"
