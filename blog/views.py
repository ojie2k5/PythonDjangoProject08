from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post
# Create your views here.

# List (dictionary)
# posts = [
    #{
    #    'author': 'CoreyMS',
    #    'title': 'Blog Post 1',
    #    'content': 'First post content 1',
    #    'date_posted': 'August 27,2021',
    #},
    #{
    #    'author': 'Jane Doe',
    #    'title': 'Blog Post 2',
    #    'content': 'First post content 2',
    #    'date_posted': 'August 28,2021',
   # },
# ]


# views has many classes that you can use to make a view page base
# on what or how you are going to use it like:
# list views - to list all blogs, or videos, or photos like home page.
# detail view - is a viewpage then you click one of the videos or photos or blog and shows a page
#             leading you to watch a video or read a blog
# delete views, update views and many more
def home(request):
    # add a dictionary example:  context = {"key", "value'}
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    # When using PostListView class you use .as_view to convert it as views
    # But it has a specific html pattern to look at <app>/<model>_<viewtype>.html
    # example: blog/post_list.html( blog - app, post - model, list - viewtype)
    # below is a code using a template to direct views to the value.
    template_name = 'blog/home.html'
    context_object_name = 'posts' # reference above the context at def home(request)
    ordering = ['-date_posted'] # newest will at the top, or date_posted for oldest at the top
    # Setting number of post per page
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    # When using PostListView class you use .as_view to convert it as views
    # But it has a specific html pattern to look at <app>/<model>_<viewtype>.html
    # example: blog/post_list.html( blog - app, post - model, list - viewtype)
    # below is a code using a template to direct views to the value.
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' # reference above the context at def home(request)
    # Setting number of post per page
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    # When using PostListView class you use .as_view to convert it as views
    # But it has a specific html pattern to look at <app>/<model>_<viewtype>.html
    # example: blog/post_list.html( blog - app, post - model, list - viewtype)
    # below is a code using a template to direct views to the value.


# LoginRequiredMixin - will redirect users to login page is they are not login
class PostCreateView(LoginRequiredMixin,  CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # Before summiting a the form it takes instance
        # setting an author equal to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)

# UserPassesTestMixin - used to prevent users updating other user's post, only the their own
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # Before summiting a the form it takes instance
        # setting an author equal to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # a redirect url to home page after button delete is submitted at delete page

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About', })