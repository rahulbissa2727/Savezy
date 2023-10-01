from django.http import HttpResponse
from . import picker

def search(request, name=None, weight=None):
    try:
        weight = int(request.GET.get('weight', weight))
    except ValueError:
        return HttpResponse("Invalid weight parameter. Weight must be an integer.")

    name = request.GET.get('name', name)
    if not name:
        return HttpResponse("Missing name parameter. Name is required.")

    results = picker.picker(name, weight)  # Call the picker function to search for the product
    return HttpResponse(results)