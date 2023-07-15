from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('tasks/',views.tasks,name='tasks'),
    path('update/<str:id>/',views.update,name='update'),
    path('delete/<str:id>/',views.delete,name='delete'),
    path('register/',views.register,name='signup'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout')

]