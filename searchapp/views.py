

# Create your views here.
# Import necessary modules
from django.shortcuts import render,get_object_or_404
from .models import  New, Booktype
from django.db.models import Q

# Define function to display all news
def new_list(request):
    news = New.objects.all()
    return render(request, 'new_list.html', {'news': news })

# Define function to display the particular new
def new_detail(request,id):
    new = get_object_or_404(New, id=id)
    return render(request, 'new_detail.html', {'new': new})

# Define function to search new
def search(request):
    results = []

    if request.method == "GET":
        query = request.GET.get('search')

        if query == '':
            query = 'None'

        results = New.objects.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query) | Q(url__icontains=query) )

    return render(request, 'search.html', {'query': query, 'results': results})