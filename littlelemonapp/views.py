from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. This is the index of the LittleLemon App.")


def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 


def drinks(request, drink_name):
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }

    choice_of_drink = drink.get(drink_name, 'Drink not available')

    return HttpResponse(f"<h2>{drink_name}</h2> + choice_of_drink")



def form_view(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, 'home.html', {'form': form})
