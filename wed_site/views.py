from django.shortcuts import render
from django.views.generic import ListView
from wed_site.models import *

menu = [{'title': 'Weddings', 'url_name': 'wed'},
        {'title': 'Lovestory', 'url_name': 'lovestory'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Contact', 'url_name': 'contact'}
        ]


class MixIn:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class Home(MixIn, ListView):
    model = MainPhotos
    queryset_all = MainPhotos.objects.order_by('id')
    queryset = queryset_all[:20]
    template_name = 'wed_site/index.html'
    context_object_name = 'photos'


class Weddings(MixIn, ListView):
    queryset = WedPost.objects.order_by('id')
    model = WedPost
    template_name = 'wed_site/wed.html'
    context_object_name = 'wed'


class ShowPost(MixIn, ListView):
    model = ImgSeries
    template_name = 'wed_site/wed_post.html'
    slug_url_kwarg = 'wedpost_slug'
    context_object_name = 'wedpost'


class Lovestory(MixIn, ListView):
    model = LoveStories
    template_name = 'wed_site/lovestories.html'
    context_object_name = 'lovest'


class Feedback(MixIn, ListView):
    model = Feedback
    queryset = Feedback.objects.order_by('-date')
    template_name = 'wed_site/about.html'
    context_object_name = 'feedback'


def about(request):
    return render(request, 'wed_site/about.html', {'menu': menu})


def contact(request):
    return render(request, 'wed_site/contact.html', {'menu': menu})
