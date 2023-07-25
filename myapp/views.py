from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import ShortenUrl
from .forms import CreateForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib import messages


class MainPageView(ListView):

    queryset = ShortenUrl.objects.order_by('-counter')
    template_name = 'myapp/main.html'
    context_object_name = "list_of_short_url"

    def post(self, request, *args, **kwargs):

        try:
            url_pk = request.POST['choice']
        except KeyError:
            return HttpResponseRedirect(reverse_lazy('shorten_url:main'))
        else:
            if request.POST['action'] == 'Delete':
                return HttpResponseRedirect(reverse_lazy('shorten_url:delete', kwargs={'pk':url_pk}))

            elif request.POST['action'] == 'Change':
                return HttpResponseRedirect(reverse_lazy('shorten_url:update', kwargs={'pk':url_pk}))


class URLDetailView(DetailView):

    model = ShortenUrl
    template_name = 'myapp/detail.html'
    context_object_name = 'url'


class CreateURLView(SuccessMessageMixin, CreateView):

    model = ShortenUrl
    form_class = CreateForm
    template_name = 'myapp/create.html'
    success_url = reverse_lazy('shorten_url:create')
    success_message = 'Successfully shorten link made.'

    def form_valid(self, form):
        post_shorten_url = form.instance.url
        if post_shorten_url == 'admin' or post_shorten_url == 'app':
            messages.error(self.request, 'You can not choose this shorten url. Please choose another one.')
            return HttpResponseRedirect(reverse_lazy('shorten_url:create'))

        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(self.request, 'This shorten url is used. Please choose a new one')
        return HttpResponseRedirect(reverse_lazy('shorten_url:create'))


class DeleteURLView(DeleteView):

    model = ShortenUrl
    success_url = reverse_lazy('shorten_url:main')
    template_name = 'myapp/delete.html'


class UpdateURLView(SuccessMessageMixin, UpdateView):

    model = ShortenUrl
    template_name = 'myapp/update.html'
    success_url = reverse_lazy('shorten_url:main')
    fields = ["url"]

    def form_valid(self, form):
        post_shorten_url = form.instance.url
        if post_shorten_url == 'admin' or post_shorten_url == 'app':
            messages.error(self.request, 'You can not choose this shorten url. Please choose another one.')
            return HttpResponseRedirect(reverse_lazy('shorten_url:update', kwargs={'pk' : self.kwargs.get('pk')}))

        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(self.request, 'This shorten url is used. Please choose a new one')
        return HttpResponseRedirect(reverse_lazy('shorten_url:update', kwargs={'pk': self.kwargs.get('pk')}))
