from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from users.models import User, Location


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']


class UserListSerializer(serializers.ModelSerializer):
    total_ads = SerializerMethodField()

    def get_total_ads(self, user):
        return user.ad_set.filter(is_published=True).count()

    class Meta:
        model = User
        fields = ['id', 'username', 'total_ads']


class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        queryset=Location.objects.all(),
        slug_field="name",
    )

    class Meta:
        model = User
        exclude = ['password']


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


# class UserCreateSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)
#     location = serializers.SlugRelatedField(
#         required=False,
#         many=True,
#         queryset=Location.objects.all(),
#         slug_field="name",
#     )
#
#     class Meta:
#         model = User
#         fields = '__all__'
#
#     def is_valid(self, raise_exception=False):
#         self._location = self.initial_data.pop("location")
#         return super().is_valid(raise_exception=raise_exception)
#
#     def create(self, validated_data):
#         user = User.objects.create(**validated_data)
#
#         for loc in self._location:
#             loc_obj, _ = Location.objects.get_or_create(name=loc)
#             user.locations.add(loc_obj)
#         user.save()
#
#         return user
