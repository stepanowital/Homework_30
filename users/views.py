import json


from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from homework_29 import settings
from users.models import User, Location
from users.serializers import UserSerializer, UserDetailSerializer, UserListSerializer, \
    LocationSerializer


class UserPagination(PageNumberPagination):
    page_size = 4


class UserListView(ListAPIView):
    queryset = User.objects.order_by("username")
    serializer_class = UserListSerializer
    pagination_class = UserPagination


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


#
# # Create your views here.
# class UserDetailView(DetailView):
#     model = User
#
#     def get(self, request, *args, **kwargs):
#         user = self.get_object()
#
#         response = {
#             "id": user.id,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#             "username": user.username,
#             "role": user.role,
#             "age": user.age,
#             "location": list(user.location.all().values_list("name", flat=True)),
#         }
#         return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})
#
#
#
#
#
# class UserCountListView(ListView):
#     model = User
#     queryset = User.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#
#         # user = User.objects.first()
#         ads = Ad.objects.all()
#
#         self.object_list = self.object_list.order_by("username")
#
#         paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
#         page_number = int(request.GET.get("page", 1))
#
#         page_obj = paginator.get_page(page_number)
#
#         users = []
#         for user in page_obj:
#             ads_user = ads.filter(author_id=user).filter(is_published=True).count()
#             users.append(
#                 {
#                     "id": user.id,
#                     "first_name": user.first_name,
#                     "last_name": user.last_name,
#                     "username": user.username,
#                     "role": user.role,
#                     "age": user.age,
#                     "locations": user.location.name,
#                     "total_ads": ads_user,
#                 }
#             )
#
#         response = {
#             "items": users,
#             "num_pages": paginator.num_pages,
#             "total": paginator.count
#         }
#
#         return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class UserCreateView(CreateView):
#     model = User
#     fields = ["first_name", "last_name", "username", "password", "role", "age"]
#     # fields = ["first_name", "last_name", "username", "password", "role", "age", "location_id"]
#
#     def post(self, request, *args, **kwargs):
#         user_data = json.loads(request.body)
#
#         user = User.objects.create(
#             first_name=user_data["first_name"],
#             last_name=user_data["last_name"],
#             username=user_data["username"],
#             password=user_data["password"],
#             role=user_data["role"],
#             age=user_data["age"]
#         )
#
#         for location in user_data["location"]:
#             location_obj, created = Location.objects.get_or_create(name=location)
#
#             user.location.add(location_obj)
#         user.save()  # Так как метод create сам всё сохранит, но скилы надо сохранить отдельно
#
#         return JsonResponse(
#             {
#                 "id": user.id,
#                 "first_name": user.first_name,
#                 "last_name": user.last_name,
#                 "username": user.username,
#                 "role": user.role,
#                 "age": user.age,
#                 "location": list(user.location.all().values_list("name", flat=True))
#             }
#         )
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ["first_name", "last_name", "username", "password", "age", "location"]
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#
#         user_data = json.loads(request.body)
#
#         self.object.first_name = user_data["first_name"]
#         self.object.last_name = user_data["last_name"]
#         self.object.username = user_data["username"]
#         self.object.password = user_data["password"]
#         self.object.age = user_data["age"]
#
#         for location in user_data["location"]:
#             location_obj, created = Location.objects.get_or_create(name=location)
#
#             self.object.location.add(location_obj)
#         self.object.save()  # Так как метод create сам всё сохранит, но скилы надо сохранить отдельно
#
#         return JsonResponse(
#             {
#                 "id": self.object.id,
#                 "first_name": self.object.first_name,
#                 "last_name": self.object.last_name,
#                 "username": self.object.username,
#                 "role": self.object.role,
#                 "age": self.object.age,
#                 "location": list(self.object.location.all().values_list("name", flat=True))
#             }
#         )
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class UserDeleteView(DeleteView):
#     model = User
#
#     success_url = "/"
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#
#         return JsonResponse({"status": "ok"}, status=200)
