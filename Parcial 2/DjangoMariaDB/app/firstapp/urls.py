from django.urls import path

from . import views

urlpatterns = [
    path('client/login',views.login,name='login'),
    path('client/list',views.showMovieList, name = 'movieList'),
    path('generate_password/<str:password>',views.makepassword,name='makepassword')
]
