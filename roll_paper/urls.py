from django.urls import path
from . import views

app_name = 'rollpaper'

urlpatterns = [
    path('userlst/', views.userlst, name='userlst'),
    path('write/', views.write, name='write'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('<int:pk>/update/', views.update, name='update'),
    

    



    

]
