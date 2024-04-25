from django.urls import path
from . import views

urlpatterns = [
    path('quote/<str:symbol>/', views.get_real_time_quotes, name='get_real_time_quotes'),
    path('historical/<str:symbol>/', views.get_historical_data, name='get_historical_data'),
    path('company/<str:symbol>/', views.get_company_info, name='get_company_info'),
    path('intraday_data/', views.get_intraday_data, name='intraday_data'),
]
