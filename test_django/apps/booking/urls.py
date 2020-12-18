from django.urls import path
from . import views

app_name = 'booking'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:booking_id>/', views.detail, name = 'detail'),
    path('<int:booking_id>/leave_comment/', views.leave_comment, name = 'leave_comment')
]
