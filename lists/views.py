from django.http import HttpResponse
from django.shortcuts import render

from lists.forms import InputToDoListItemForm


home_page=None
def home_page(request):
    form = InputToDoListItemForm()

    context={'item_text': 'Test'}

    if request.method == 'POST':
        context={'new_item_text': request.POST.get('item_text', '')}

    return render(request, 'lists/home.html', context)


