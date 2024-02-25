from django.urls import path
from . import views


app_name='pictures'
urlpatterns=[
    path('', views.index, name='index'),
    path('picture<int:picture_id>/',views.detail, name='details'),
    path('video<int:video_id>/',views.detailtwo,name='detailsvideo'),
    path('track<int:track_id>',views.detailone,name='detailstrack'),
    ]

# gallery/urls.py

