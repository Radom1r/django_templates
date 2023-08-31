from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipe(request, meal_name):
    amount = int(request.GET.get('servings', 1))
    meal = DATA[meal_name]
    ingredients_amount = {}
    for index in meal.items():
        ingredients_amount[index[0]] = round(index[1] * amount, 2)
    context = {
        'recipe':ingredients_amount
    }
    return render(request, 'calculator/index.html', context=context)