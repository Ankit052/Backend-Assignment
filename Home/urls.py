from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('users',views.UserListCreate.as_view()),
    path('users/<int:pk>',views.UserRetrieveUpdateDestroy.as_view())

]
