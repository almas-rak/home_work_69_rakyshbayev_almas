from django.urls import path

from webapp.api_calc import calc
from webapp.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', calc, name='add'),
    path('subtract/', calc, name='subtract'),
    path('multiply/', calc, name='multiply'),
    path('divide/', calc, name='divide')
]
