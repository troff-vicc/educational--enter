from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(label_suffix=False, label='', max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Логин',
                                                        'autocomplete': "off"}))
    password = forms.CharField(label_suffix=False, label='', max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Пароль',
                                                            'autocomplete': "off"}))