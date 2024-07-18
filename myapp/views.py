from django.shortcuts import render
from myapp.models import Review

def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, template_name="index.html", context=context)
