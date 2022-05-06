from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='posts_detail'),
    path('category/<slug:pk>/', views.CategoryView.as_view(), name='category'),
    # path('search/', views.Search.as_view(), name='search'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
]
