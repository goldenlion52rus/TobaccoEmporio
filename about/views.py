from django.shortcuts import render


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]


def about(request):
    return render(request, 'about/about.html', {'title': 'О сайте', 'menu': menu})
