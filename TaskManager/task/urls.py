from django.urls import path
from .  import views
urlpatterns = [
    path('',views.main,name='main'),
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('dashboard/',views.board,name='board'),
    path('logout/',views.Logout,name='logout'),
    path('main/',views.main,name= 'main'),
    path('common/',views.Common,name= 'common'),
    path('update_task/<str:pk>/',views.Update, name="update_task"),
    path('del/<str:pk>/',views.Delete, name="del"),
    # path('dashboard/<str:pk>/',views.task_emp,name='task_emp')
]