from django import forms

class InputToDoListItemForm(forms.Form):
    input_klingon = forms.CharField(label="Enter", max_length=255, initial=' ')