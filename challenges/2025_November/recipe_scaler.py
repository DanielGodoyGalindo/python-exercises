"""
Recipe Scaler
Given an array of recipe ingredients and a number to scale the recipe, return an array with the quantities scaled accordingly.

Each item in the given array will be a string in the format: "quantity unit ingredient". For example "2 C Flour".
Scale the quantity by the given number. Do not include any trailing zeros and do not convert any units.
Return the scaled items in the same order they are given.
"""


def scale_recipe(ingredients, scale):
    output = []
    for ingredient in ingredients:
        index = ingredient.find(" ")
        quantity = float(ingredient[:index]) * scale
        new_ingredient = str(quantity).removesuffix(".0") + ingredient[index:]
        output.append(new_ingredient)
    return output


print(scale_recipe(["2 C Flour", "1.5 T Sugar"], 2))
