from .models import Blog
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the blogs
        context['latest_posts'] = Blog.objects.all()[:5]
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog_detail'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the blogs
        context['latest_posts'] = Blog.objects.all()[:5]
        return context
