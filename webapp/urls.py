from django.urls import path

from webapp.api_calc import calc, get_token_view
from webapp.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', calc, name='add'),
    path('subtract/', calc, name='subtract'),
    path('multiply/', calc, name='multiply'),
    path('divide/', calc, name='divide'),
    path('token/', get_token_view, name='divide')
]


