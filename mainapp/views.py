from django.shortcuts import render


# Create your views here.
def index(request):
    info = [
        ['Карбонара', 'carbonara',
         'Бекон, сыры чеддер и пармезан, моцарелла, томаты черри, красный лук, чеснок, соус альфредо, итальянские травы'],

        ['Четыре сыра', 'four_cheeses',
         'Сыр блю чиз, сыры чеддер и пармезан, моцарелла, соус альфредо'],

        ['Ветчина и сыр', 'ham_and_cheese',
         'Ветчина, моцарелла, соус альфредо'],

        ['Ветчина и грибы', 'ham_and_mushrooms',
         'Ветчина, шампиньоны, увеличенная порция моцареллы, томатный соус'],

        ['Пепперони', 'pepperoni',
         'Пикантная пепперони, увеличенная порция моцареллы, томатный соус'],
    ]
    return render(request, 'mainapp/index.html', {'info': info})


def basket_page(request):
    return render(request, 'mainapp/basket_page.html')