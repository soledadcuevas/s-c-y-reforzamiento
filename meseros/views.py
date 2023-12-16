from django.shortcuts import render

# Create your views here.
def meseros_list(request):

    data_context = {
        'nombre': 'Luis Pardo',
        'pais': 'Perú',
        'edad': 24,
    }
    return render(request,'meseros_list.html', context={'data': data_context})