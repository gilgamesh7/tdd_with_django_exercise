import re
from django.shortcuts import render

from lists.forms import InputToDoListItemForm


home_page=None
def home_page(request):
    form = InputToDoListItemForm()

    context={'form': form}

    return render(request, 'lists/home.html', context)


