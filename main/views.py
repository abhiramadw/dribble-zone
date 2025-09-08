from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406358043',
        'name': 'Pria Abhirama Dewa',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)