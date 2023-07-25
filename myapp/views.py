from django.shortcuts import render
from .models import ShortenUrl
from .forms import CreateForm, UpdateMainForm, UpdateShortenForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q


def mainview(request):
    if request.method == 'POST':
        try:
            url_id = request.POST['choice']
        except KeyError:
            pass
        else:
            if request.POST['action'] == 'Delete':
                ShortenUrl.objects.get(pk=url_id).delete()

            elif request.POST['action'] == 'Change':
                return HttpResponseRedirect('/app/' + str(url_id))

    shorten_urls = ShortenUrl.objects.all()
    return render(request, 'myapp/main.html', {'list_of_short_url': shorten_urls})


def createview(request):

    message = ''
    if request.method == 'POST':
        form = CreateForm(request.POST)

        if form.is_valid():
            post_shorten_url = form.cleaned_data['url']
            post_main_url = form.cleaned_data['original_url']
            if ShortenUrl.objects.filter(url=post_shorten_url).count() > 0:
                message = 'This shorten url is used. Please choose a new one'
            elif post_shorten_url == 'admin' or post_shorten_url == 'app':
                message = 'You can not choose this shorten url. Please choose another one.'

            else:
                ShortenUrl.objects.create(url=post_shorten_url, original_url=post_main_url)
                message = 'Successfully shorten link made.'

    form = CreateForm()
    return render(request, 'myapp/create.html', {'form': form, 'message': message})


def updateview(request, url_id):
    return render(request, 'myapp/update.html', {'url_id' : url_id})


def updatemain(request, url_id):
    if request.method == 'POST':
        form = UpdateMainForm(request.POST)
        if form.is_valid():
            post_main_url = form.cleaned_data['url']
            update_url = ShortenUrl.objects.get(pk=url_id)
            update_url.original_url = post_main_url
            update_url.save()

    form = UpdateMainForm({'url' : ShortenUrl.objects.get(pk=url_id).original_url})
    return render(request, 'myapp/update_main.html', {'form': form})


def updateshorten(request, url_id):
    message = ''
    if request.method == 'POST':
        form = UpdateShortenForm(request.POST)

        if form.is_valid():
            post_shorten_url = form.cleaned_data['url']
            if ShortenUrl.objects.filter(url=post_shorten_url).exclude(pk=url_id).count() > 0:
                message = 'This shorten url is used. Please choose a new one'
            elif post_shorten_url == 'admin' or post_shorten_url == 'app':
                message = 'You can not choose this shorten url. Please choose another one.'
            else:
                updated_url = ShortenUrl.objects.get(pk=url_id)
                updated_url.url = post_shorten_url
                updated_url.save()
                message = 'Successfully update shorten name'

    form = UpdateShortenForm({'url' : ShortenUrl.objects.get(pk=url_id).url})
    return render(request, 'myapp/update_shorten.html', {'form': form, 'message': message})
