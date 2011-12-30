from django.shortcuts import render


def main(request):
    return render(request, 'web/main.html', locals())
