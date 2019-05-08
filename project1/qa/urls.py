from django.urls import path
from . import views

app_name = 'qa'

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'), #/qa
  path('about', views.about, name='about'), #/qa/about
  path('player', views.player, name='player'), #/qa/player
  path('add/', views.AddView.as_view(), name='add'), #/qa/add
  path('update/<int:pk>', views.UpdateView.as_view(), name='update'), #qa/update/1
  path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'), #qa/delete/1
  path('detail/<int:pk>', views.DetailView.as_view(), name='detail'), #qa/detail/1
  path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
  path('comment/<int:day_pk>', views.CommentView.as_view(), name='comment'),
]
