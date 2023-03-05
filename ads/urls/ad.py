from django.urls import path

from ads.views import AdDetailView, AdListCreateView

urlpatterns = [
    path('<int:pk>', AdDetailView.as_view()),
    path('', AdListCreateView.as_view()),
]