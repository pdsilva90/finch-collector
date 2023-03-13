from django.shortcuts import render

# Create your views here.
finches = [
  {'name': 'Mongo', 'breed': 'European Goldfinch', 'description': 'Always hungry', 'age': 5},
  {'name': 'Baloo', 'breed': 'Blue Finch', 'description': 'Beautiful singer', 'age': 3},
  {'name': 'Mavis', 'breed': 'Owl Finch', 'description': 'Very talkative', 'age': 2},
]

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finch_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })