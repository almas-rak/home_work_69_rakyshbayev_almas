from django.urls import path

from task1.api_calc import calc

urlpatterns = [
    path('add/', calc, name='add'),
    path('subtract/', calc, name='subtract'),
    path('multiply/', calc, name='multiply'),
    path('divide/', calc, name='divide')
]