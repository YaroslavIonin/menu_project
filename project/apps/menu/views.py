from django.shortcuts import render


def index(request):
    return render(request, "base.html")


def main(request, slugs=None):
    return render(request, "base.html", {
        'request': request
    })

