from django import  forms

class formulariLogin(forms.Form):
    usuari = forms.CharField(max_length=100, label="Usuari")
    contrasenya = forms.CharField(max_length=100, label="Contrasenya", widget=forms.PasswordInput() )

class formulariCanvi(forms.Form):
    novaContrasenya1 = forms.CharField(max_length=100, label="Nova contrasenya", widget=forms.PasswordInput() )
    novaContrasenya2 = forms.CharField(max_length=100, label="Repeteix la nova contrasenya", widget=forms.PasswordInput() )