from django.urls import path

from ads.views import AdDetailView, AdListView, AdCreateView, AdUpdateView, AdDeleteView

urlpatterns = [
    path('<int:pk>', AdDetailView.as_view(), name='ad_detail'),
    path('', AdListView.as_view(), name='ad_list'),
    path('create/', AdCreateView.as_view(), name='ad_list'),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad_update'),
]