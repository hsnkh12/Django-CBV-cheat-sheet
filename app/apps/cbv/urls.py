from django.urls import path,include
from .views import IndexView,LinkPreloadView

urlpatterns = [
    path('',IndexView.as_view(),name='index')
]