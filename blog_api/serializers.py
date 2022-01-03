from rest_framework import serializers
from blog.models import Post, Category
from django.conf import settings



class PostSerializer(serializers.ModelSerializer):          # jahile child table ko serializer ko code suru ma lekhne ani ball Parent table ko serializer code lekhne
    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'author', 'image', 'slug', 'excerpt', 'content', 'status')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}


# CategoryPostSerializer hamile banayeko auta custom non related multiple serializer
class CategoryPostSerializer(serializers.Serializer):
    posts = PostSerializer(many=True)
    categories = CategorySerializer(many=True)