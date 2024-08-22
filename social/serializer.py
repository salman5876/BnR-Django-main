from rest_framework import serializers

from social import retrieve_user_data

from .models import *


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'


class NeighborhoodFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighborhoodFollower
        fields = '__all__'


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = ['media']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user_data = serializers.SerializerMethodField()
    total_likes = serializers.SerializerMethodField()

    def get_user_data(self, comment):
        return retrieve_user_data(comment.commented_by, self.context['request'])

    def get_total_likes(self, comment):
        return comment.comment_likes.count()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        del data['commented_by']
        del data['post']
        return data

    class Meta:
        model = Comment
        fields = '__all__'


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user_data = serializers.SerializerMethodField()
    neighborhood_data = serializers.SerializerMethodField()
    media_list = MediaSerializer(many=True, required=False)
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    comments_list = serializers.SerializerMethodField()

    def get_user_data(self, post):
        return retrieve_user_data(post.user, self.context['request'])

    def get_neighborhood_data(self, post):
        neighborhood = post.neighborhood
        if neighborhood:
            neighborhood_data = {
                'id': neighborhood.id,
                'name': neighborhood.name
            }
            return neighborhood_data
        else:
            return 'No neighborhood found at this location'

    def get_comments_list(self, post):
        comments = post.comments_list.order_by('-id')[:3]
        comment_serializer = CommentSerializer(comments, many=True, context={'request': self.context['request']})
        return comment_serializer.data

    def get_total_likes(self, post):
        return post.post_likes.count()

    def get_total_comments(self, post):
        return post.comments_list.count()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        del data['user']
        del data['neighborhood']
        return data

    class Meta:
        model = Post
        fields = '__all__'


class ConnectionRequestSerializer(serializers.ModelSerializer):
    user_data = serializers.SerializerMethodField()

    def get_user_data(self, connection_request):
        context_type = self.context['type']
        if context_type == 'pending_requests':
            user = connection_request.sent_by
        elif context_type == 'sent_requests':
            user = connection_request.sent_to
        return retrieve_user_data(user, self.context['request'])

    def to_representation(self, instance):
        data = super().to_representation(instance)
        del data['sent_by']
        del data['sent_to']
        return data

    class Meta:
        model = ConnectionRequest
        fields = '__all__'


class ConnectionSerializer(serializers.ModelSerializer):
    user_data = serializers.SerializerMethodField()

    def get_user_data(self, connection):
        user_one, user_two = connection.user_one, connection.user_two
        other_user = user_one if user_one.id != self.context['user'] else user_two
        return retrieve_user_data(other_user, self.context['request'])

    def to_representation(self, instance):
        data = super().to_representation(instance)
        del data['user_one']
        del data['user_two']
        return data

    class Meta:
        model = Connection
        fields = '__all__'
