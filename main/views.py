from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Aryan Primasatya Putra Hidayat',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
