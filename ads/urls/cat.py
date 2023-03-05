from django.urls import path

from ads.views import CategoryDetailView, CategoryListCreateView

urlpatterns = [
    path('<int:pk>', CategoryDetailView.as_view()),
    path('', CategoryListCreateView.as_view()),
]