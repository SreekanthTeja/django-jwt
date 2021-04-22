from django.urls import path
from posts.views import *

urlpatterns = [
    path('all',PostListView.as_view(),name='list-api'),
    path('create',PostCreateView.as_view(),name='create-api'),
    path('rud/<int:pk>',RUDPostView.as_view(),name='rud-api'),
]