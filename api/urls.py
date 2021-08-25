from django.urls import path
from . import views

urlpatterns = [
    #path('', views.apiOverview, name='apiOverview'),
    path('movie-list/', views.allMovie, name='movie-list'),
    path('search-movie/<str:name>', views.viewMovie, name='search-movie'),
    path('create-comment/', views.createComment, name='create-comment'),
    path('comment-list/', views.allComments, name='comment-list'),
    path('search-comment/<int:pk>', views.viewComment, name='comment'),
]