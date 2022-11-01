from django.shortcuts import render


def show_partnership(request):
    return render(request, "partnership.html")