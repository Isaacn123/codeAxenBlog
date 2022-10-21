from django.urls import path, include
from  . import views


urlpatterns = [
     path('', views.PostIndexView.as_view(), name = 'home'),
     path('<slug:slug>/', views.PostIndexView.as_view(), name = 'post_detail')
]
