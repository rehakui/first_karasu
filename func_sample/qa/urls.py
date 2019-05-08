from django.urls import path
from . import views

app_name = 'qa'

urlpatterns = [
  path('', views.index, name='index'), #/qa
  path('about', views.about, name='about'), #/qa/about
  path('add/', views.add, name='add'), #/qa/add
  path('update/<int:pk>', views.update, name='update'), #qa/update/1
  path('delete/<int:pk>', views.delete, name='delete'), #qa/delete/1
  path('detail/<int:pk>', views.detail, name='detail'), #qa/detail/1
]
