"""Platzigram URL's module"""

from django.urls import path

from platzigram import views as local_views

from posts import views as posts_views

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('hi/', local_views.hi),
    path('sorted/', local_views.sorted),
    path('personal/<str:name>/<int:age>/', local_views.personal),

    path('posts/', posts_views.list_posts)
]
