from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 100,
        'сыр, г': 50,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
    },
}

def home_view(request):
    return HttpResponse(
        'Доступные рецепты: /omlet/ , /pasta/ , /buter/'
    )

def recipe_view(request, dish):
    recipe = DATA.get(dish)

    if recipe is None:
        return render(request, 'calculator/index.html', {'recipe': {}})

    servings = request.GET.get('servings')
    if servings:
        servings = int(servings)
        recipe = {k: v * servings for k, v in recipe.items()}

    return render(request, 'calculator/index.html', {'recipe': recipe})
