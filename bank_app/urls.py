from .import views
from django.urls import path
app_name='bank_app'
urlpatterns = [
     path('',views.home, name="home"),
     path('membership', views.membership, name='membership'),
     path('get-branches/', views.get_branches, name='get_branches'),

]