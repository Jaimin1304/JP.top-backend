from django.shortcuts import render

def gswar(request):
    return render(request, "gswar/gswar.html", {})
