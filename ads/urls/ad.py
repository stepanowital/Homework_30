from django.urls import path
from rest_framework import routers

from ads.views import AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, AdImageView, AdViewSet


router = routers.SimpleRouter()
router.register('', AdViewSet)

urlpatterns = [
    path('<int:pk>', AdDetailView.as_view(), name='ad_detail'),
    # path('', AdListView.as_view(), name='ad_list'),
    path('create/', AdCreateView.as_view(), name='ad_list'),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad_update'),
    path('<int:pk>/upload_image/', AdImageView.as_view(), name='as_image'),
]

urlpatterns += router.urls
