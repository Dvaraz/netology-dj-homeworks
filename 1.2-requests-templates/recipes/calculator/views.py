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
    # можете добавить свои рецепты ;)
}


def recipe_view(request, recipe):
    """
    Попробовал написать одну view для всех рецептов используя параметр url.
    try exept использовал, что бы не было ошибки  если в параметрах url был введен рецепт которого нет в
    DATA.
    """
    servings = int(request.GET.get('servings', 1))
    try:
        context = {
            'recipe': {i: DATA[recipe][i] * servings for i in DATA.get(recipe)}
        }
    except TypeError as err:
        context = {}
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
