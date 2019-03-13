from django.urls import path

from . import views
from books import views as books_views

urlpatterns = [

	## all urls needs trailing slashes

	## /api/v1/ 	---> list all books 
	## /api/v1/		---> POST new books 
	##						- form-data: 	-title
	##										-book_author
	##										-summary	
    path('', views.ListBooks.as_view()),

	## /api/v1/		---> POST new books 
    path('', books_views.PostCreateView.as_view(), name='post-create'),

    ## /api/v1/7/	---> GET - list a singular book based on id 
    ## /api/v1/7/	---> PUT - updated book information using form-data fields
    ## /api/v1/7/	---> DELETE - delete book information using form-data fields
   	##							- needs trailing slash in url
    path('<int:pk>/', views.DetailBook.as_view()),
]