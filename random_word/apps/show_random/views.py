from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def show_random(request):
    if 'number' not in request.session:
        request.session['number'] = 0
    if request.method == "POST":
        request.session['number'] += 1
    word = get_random_string(length=12)
    context = {
        'number': request.session['number'],
        'word': word
    }
    return render(request, 'show_random/index.html', context)


def reset(request):
    request.session['number'] = 0
    return redirect('/random_word/')