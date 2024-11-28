from django.urls import path
from . import views
from .views import LiveStreamListView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('api/live-streams/', LiveStreamListView.as_view(), name='live_stream_list'),

]
