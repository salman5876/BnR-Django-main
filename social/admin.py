from django.contrib import admin

from .models import *


class NeighborhoodFollowersInline(admin.StackedInline):
    model = NeighborhoodFollower
    extra = 0


class PostsInline(admin.StackedInline):
    model = Post
    extra = 0
    fields = ['id']


class MediaInline(admin.StackedInline):
    model = Media
    extra = 0


class PostLikesInline(admin.StackedInline):
    model = PostLike
    extra = 0


class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 0
    fields = ['commented_by']


class CommentLikesInline(admin.StackedInline):
    model = CommentLike
    extra = 0


class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'state', 'latitude', 'longitude']
    search_fields = ['name', 'state']
    inlines = [PostsInline, NeighborhoodFollowersInline]


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'user', 'neighborhood_name', 'state']
    search_fields = ['user__username', 'neighborhood__name', 'state']
    inlines = [MediaInline, PostLikesInline, CommentsInline]

    def neighborhood_name(self, post):
        return post.neighborhood.name


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'commented_by', 'post_by']
    search_fields = ['commented_by__username', 'post__user__username']
    inlines = [CommentLikesInline]

    def post_by(self, comment):
        return comment.post.user.username


class ConnectionRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'sent_by', 'sent_to']
    search_fields = ['sent_by__username', 'sent_to__username']


class ConnectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_one', 'user_two']
    search_fields = ['user_one__username', 'user_two__username']


admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ConnectionRequest, ConnectionRequestAdmin)
admin.site.register(Connection, ConnectionAdmin)
