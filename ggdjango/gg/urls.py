
from django.urls import path
from . import views

#localhost:8000/gg
#localhost: 8000/gg/order
urlpatterns = [
    path('', views.all_gg, name='all_gg'),
    path('<int:momo_id>/', views.gg_detail, name='gg_detail'),
]
