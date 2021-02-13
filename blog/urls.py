
from django.urls import path
from . import views

urlpatterns = [
 #     path('', views.index),

      path('', views.post_list, name='post_list'),
      path('new', views.new),
      path('urltest', views.urltest),
]
