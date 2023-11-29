from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "edr/index.html", context)

def disclaimer(request):
    context = {}
    return render(request, "edr/disclaimer_screen.html", context)

def assess(request):
    context = {}
    return render(request, "edr/assess_screen.html", context)

def list(request):
    context = {}
    return render(request, "edr/list_screen.html", context)