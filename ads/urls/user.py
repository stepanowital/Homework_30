from django.urls import path

from users.views import UserDetailView, UserListView, UserCreateView, UserCountListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('', UserListView.as_view(), name='user_list'),
    path('Z/', UserCountListView.as_view(), name='user_count_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]