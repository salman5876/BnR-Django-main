from django.urls import path

from . import views


urlpatterns = [
    path('create_post/', views.create_post),
    path('get_neighborhoods/', views.get_neighborhoods),
    path('follow_neighborhood/', views.follow_neighborhood),
    path('get_posts/', views.get_posts),
    path('like_post/', views.like_post),
    path('create_comment/', views.create_comment),
    path('get_post_comments/<int:pk>', views.get_post_comments),
    path('like_comment/', views.like_comment),
    path('edit_comment/', views.edit_comment),
    path('delete_comment/', views.delete_comment),
    path('send_request/', views.send_connection_request),
    path('accept_request/', views.accept_connection_request),
    path('get_connections/<int:pk>', views.get_connections),
    path('get_sent_requests/<int:pk>', views.get_sent_connection_requests),
    path('get_pending_requests/<int:pk>', views.get_pending_connection_requests)
]
