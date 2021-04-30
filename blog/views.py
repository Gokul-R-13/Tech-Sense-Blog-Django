from django.views import generic
from django.views.generic import ListView,DetailView,CreateView
from .models import Post,Category
from .forms import CommentForm,postForm,ContactForm
from django.urls import reverse,reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class AddPostView(CreateView):
    model = Post
    form_class = postForm
    template_name = 'add_post.html'


def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
        
    else:
        f = ContactForm()
    return render(request, 'contact.html', {'form': f})
   
def aboutus(request):
   return render(request, "aboutus.html")

def CategoryView(request, cats):
    category_posts=Post.objects.filter(category=cats)
    return render(request,'categories.html', {'cats':cats.title(), 'category_posts':category_posts})


def post_detail(request, slug):

    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
    