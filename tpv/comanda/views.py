from django.shortcuts import render

# Create your views here.
@login_required
def llistarComandes(request):
    comandes = Comanda.objects.all()
    context = { 'comandes' : categories }
    return render(request, 'llistaCategories.html', context)