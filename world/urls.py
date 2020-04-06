from django.urls import path

from .views import IndexView, ProjectView, ReviewDetialView

app_name = 'world'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project'),
    path('review/<int:pk>/', ReviewDetialView.as_view(), name='review'),
]