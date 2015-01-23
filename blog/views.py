import random
from django.shortcuts import render
from .models import Post

#python manage.py shell > may have to install ipython

# Create your views here.
def post_list(request): # simple view, accepts requests

	# post = Post.objects.all() # REtrieve all posts even unpublished ones
	posts = Post.objects.filter(published_date__isnull=False)
	# post = [post for post in posts]

	return render(request, 'blog/post_list.html', {
			'post' : posts
	}) #blog/post template

