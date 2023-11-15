from django import forms


class AdminPanelForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control',
                                                         'type': 'file',
                                                         'id': 'formFile'}))
