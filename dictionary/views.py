from django.shortcuts import render, HttpResponse
from pydictionary import Dictionary
# Create your views here.

def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def results(request):
    value = request.POST.get('value')
    word = value
    dictionary = Dictionary(value)
    meaning = dictionary.meanings()
    synonyms = dictionary.synonyms()
    antonyms = dictionary.antonyms()
    context = {
        'word': word,
        'meaning': meaning,
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    return render(request, 'results.html', context)
