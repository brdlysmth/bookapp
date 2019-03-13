from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post 
from rest_framework import generics 
# from django.http import HttpResponse

# Create your views here.


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'books/home.html', context)


## List View
class PostListView(ListView):
	model = Post
	template_name = 'books/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

## Detail View
class PostDetailView(DetailView):
	model = Post
	template_name = 'books/post_detail.html'

## Create View // Add Book 
class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'book_author', 'summary']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
## Update View 
class PostUpdateView(UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'book_author', 'summary']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	# TODO: make sure only the author of the post can edit a post 

	def test_func(self):						
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

## Delete View
class PostDeleteView(UserPassesTestMixin, DeleteView):
	model = Post
	success_url = "/"					## upon deletion, send user to the home page

	# TODO: make sure only the author of the post can edit a post 

	def test_func(self):						
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

## Simple About Page
def about(request):

	return render(request, 'books/about.html', { 'title': 'about' })







