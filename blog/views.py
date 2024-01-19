from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from blog.models import Blog
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy


#ВСЕ БЛОГИ
class BlogListView(ListView):
    model = Blog

#ДЕТАЛИ
class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        slug = self.kwargs.get('slug')
        return get_object_or_404(Blog, slug=slug)

#СОЗДАНИЕ
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'ispublished', 'preview')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Blog, slug=slug)

    def get_success_url(self):
        return reverse_lazy('blog:blogdetail', kwargs={'slug': self.object.slug})

#РЕДАКТИРОВАНИЕ
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'ispublished', 'preview')
    slug = 'slug'

    def get_success_url(self):
        return reverse_lazy('blog:bloglist')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Blog, slug=slug)

#УДАЛЕНИЕ
class BlogDeleteView(DeleteView):
    model = Blog
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Blog, slug=slug)

    def get_success_url(self):
        return reverse_lazy('blog:bloglist')

#АКТИВИРОВАНО-ДЕАКТИВИРОВАНО
def active(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if blog.ispublished:
        blog.ispublished = False
    else:
        blog.ispublished = True
    blog.save()
    return redirect(reverse('blog:bloglist'))
