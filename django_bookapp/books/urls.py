#./books/urls.py
#	#	#	#	#	#	#	#	#	
from django.urls import path
from .views import (PostListView, 
	PostDetailView, 
	PostCreateView, 
	PostUpdateView, 
	PostDeleteView,
	)
from . import views 

urlpatterns = [
    # path('', views.home, name='books-home'),
    path('', PostListView.as_view(), name='books-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),			## read book
    path('post/new/', PostCreateView.as_view(), name='post-create'),				## create book
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),	## update book
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),	## delete book
    path('about/', views.about, name='books-about')
]
