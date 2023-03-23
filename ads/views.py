import json


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView


from ads.models import Category, Ad
from users.models import User


# Create your views here.
def root(request):
    return JsonResponse({"status": "ok"})


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        response = {
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author.id,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
            "category_id": ad.category.id,
            "category": ad.category.name
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


class AdListView(ListView):
    model = Ad
    queryset = Ad.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("id")

        response = []
        for ad in self.object_list:
            response.append({
                "id": ad.id,
                "name": ad.name,
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    model = Ad
    fields = ["name", "author_id", "price", "description", "address", "is_published", "category_id"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data["name"],
            author_id=ad_data["author_id"],
            price=ad_data["price"],
            description=ad_data["description"],
            address=ad_data["address"],
            is_published=ad_data["is_published"],
            category_id=ad_data["category_id"]
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
            "category": ad.category.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    model = Ad
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)

        self.object.name = category_data["name"]
        self.object.author_id = category_data["author_id"]
        self.object.price = category_data["price"]
        self.object.description = category_data["description"]
        self.object.address = category_data["address"]
        self.object.is_published = category_data["is_published"]
        self.object.category_id = category_data["category_id"]

        self.object.save()

        return JsonResponse(
            {
                "id": self.object.id,
                "name": self.object.name,
                "author": self.object.author.username,
                "price": self.object.price,
                "description": self.object.description,
                "address": self.object.address,
                "is_published": self.object.is_published,
                "category": self.object.category.name
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):
    model = Ad

    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("id")

        response = []
        for category in self.object_list:
            response.append({
                "id": category.pk,
                "name": category.name,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        response = {
            "id": category.pk,
            "name": category.name,
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category = Category.objects.create(**category_data)

        return JsonResponse(
            {
                "id": category.id,
                "name": category.name
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)

        self.object.name = category_data["name"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category

    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)

