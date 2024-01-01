from . import views
from django.urls import path

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbv/', views.TaskListView.as_view(), name='cbv'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),


]
