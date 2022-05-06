from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .models import Post, Category
from .forms import ReviewForm


# Create your views here.


class PostList(View):
    def get(self, request):
        posts = Post.objects.filter(is_published=True).select_related('category')
        category = Category.objects.all()
        return render(request, 'articles/index.html', {'post_list': posts, 'categories': category, 'cat_selected': 0})


class PostDetail(View):
    def get(self, request, slug):
        posts = Post.objects.get(url=slug)
        return render(request, 'articles/single_post.html', {'post': posts})


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.post = post
            form.save()
        return redirect(post.get_absolute_url())


class CategoryView(View):
    def get(self, request, pk):
        posts = Post.objects.filter(is_published=True).select_related('category')
        category = Category.objects.all()
        context = {'post_list': posts,
                   'categories': category,
                   'cat_selected': pk
                   }
        return render(request, 'articles/index.html', context)

class Search(ListView):
    template_name = 'articles/index.html'
#
#     def get_queryset(self):
#         return Post.objects.filter(title__icontains=self.request.GET.get('q'))
#
#     def get_context_data(self, *args, **kwargs):
#         try:
#             context = super().get_context_data(*args, **kwargs)
#             context['q'] = self.request.GET.get('q')
#         except:
#             context = None
#         return context
