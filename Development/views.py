from django.shortcuts import render


def development_list(request):
    return render(request, 'development_list.html', {})
