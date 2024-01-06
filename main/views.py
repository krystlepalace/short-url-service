from django.shortcuts import render, redirect
from main.models import Tokens
from main.forms import URLForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.method == 'POST':
        linkform = URLForm(request.POST)
        
        if linkform.is_valid():
            if Tokens.objects.filter(full_link=linkform.cleaned_data['full_link']).exists():
                link = Tokens.objects.get(full_link=linkform.cleaned_data['full_link'])
            else:
                Tokens.objects.create(full_link=linkform.cleaned_data['full_link']).save()
                link = Tokens.objects.get(full_link=linkform.cleaned_data['full_link'])

            return render(request, 'main/partials/link.html', {'link': link })

    data = {
        'title': 'ShortURL',
        'form': URLForm
    }

    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'krystlepalace'
    }

    return render(request, 'main/about.html', data)

def redirect_to_original(request, slug):
    original = Tokens.objects.get(short_link=slug).full_link
    
    return redirect(original)
