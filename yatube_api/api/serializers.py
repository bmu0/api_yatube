from rest_framework import serializers

from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        extra_kwargs = {"author": {"required": False, "allow_null": True}}


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'post', 'created', 'author')
        extra_kwargs = {"author": {"required": False, "allow_null": True}}

    def get_post(self, obj):
        post = int(obj.post.id)
        return post