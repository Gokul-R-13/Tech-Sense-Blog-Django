from . import views
from django.urls import path

urlpatterns = [
	path('', views.PostList.as_view(), name='home'),
	path('aboutus/', views.aboutus, name='aboutus'),
	path('contact/', views.contact, name='contact'),
	path('add_post/', views.AddPostView.as_view(), name='add_post'),
	path('category/<str:cats>/',views.CategoryView, name='category'),
	path('<slug:slug>/', views.post_detail, name='post_detail'),

]