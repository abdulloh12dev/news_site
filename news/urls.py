from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('single/<str:news_slug>/', single_page, name='single'),
    path('category/<str:category_slug>/', category_page, name='category'),
    path('contact/', contact_page, name='contact'),
    path('send-message/', contact_page, name='send_message_to_telegram'),

]