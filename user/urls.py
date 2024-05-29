from django.urls import path
from . import views


urlpatterns = [
    path('account/', views.account, name='account'),
    path('update/', views.info_update, name='update'),
]
