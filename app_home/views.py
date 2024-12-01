from django.shortcuts import render


# Create your views here.
def index(request):

    context = {
        # 'text': 'Inicial',
        'title': 'Home'
    }

    return render(request, 'app_home/index.html', context)