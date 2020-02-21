from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
]


