from django.db.models import Q
from geopy.distance import distance
from geopy.geocoders import Nominatim
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializer import *
from .models import *


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_post(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['user'] = data['user_id']
        del data['user_id']
        if not User.objects.filter(pk=data['user']).exists():
            return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        post_lat, post_long = float(request.data['latitude']), float(request.data['longitude'])
        try:
            geolocator = Nominatim(user_agent="BnR")
            location = geolocator.reverse(f"{post_lat}, {post_long}")
            address = location.raw['address']
            required_places = ['neighbourhood', 'village', 'hamlet', 'building', 'amenity']
            for place in required_places:
                if place in address:
                    address['name'] = address[place]
                    break
            latitude = location.latitude
            longitude = location.longitude
            neighborhood = {
                'name': address.get('name', request.data['area_address']),
                'state': address.get('state', request.data['state']),
                'latitude': latitude if latitude else post_lat,
                'longitude': longitude if longitude else post_long
            }
        except:
            neighborhood = None

        # The following code can be used to generate neighborhoods data using Google geocoding API

        # api_key = 'PUT YOUR API KEY HERE'
        # client = Client(api_key)
        # reverse_geocode_result = client.reverse_geocode((post_lat, post_long))
        # for component in reverse_geocode_result:
        #     if 'neighborhood' in component['types']:
        #         for sub_component in component['address_components']:
        #             if 'administrative_area_level_1' in sub_component['types']:
        #                 neighborhood = {
        #                     'name': component['address_components'][0]['long_name'],
        #                     'state': sub_component['long_name'],
        #                     'latitude': component['geometry']['location']['lat'],
        #                     'longitude': component['geometry']['location']['lng']
        #                 }
        #                 break
        #         break

        if neighborhood:
            try:
                data['neighborhood'] = Neighborhood.objects.get(name=neighborhood['name']).id
            except:
                neighborhood_serializer = NeighborhoodSerializer(data=neighborhood)
                if neighborhood_serializer.is_valid():
                    new_neighborhood = neighborhood_serializer.save()
                    data['neighborhood'] = new_neighborhood.id
                else:
                    return Response(neighborhood_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            data['neighborhood'] = ''
        post_serializer = PostSerializer(data=data)
        if post_serializer.is_valid():
            post = post_serializer.save()
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        media_files = request.FILES.getlist('media')
        for file in media_files:
            post_media = Media()
            post_media.post = Post.objects.get(pk=post.id)
            post_media.media = file
            post_media.save()
        return Response({'detail': 'Successfully Posted'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
def get_neighborhoods(request):
    if request.method == 'POST':
        neighborhoods = Neighborhood.objects.filter(state=request.data['state'])
        serializer = NeighborhoodSerializer(neighborhoods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
def follow_neighborhood(request):
    if request.method == 'POST':
        try:
            user_id = User.objects.get(pk=request.data['user_id']).id
            neighborhood = Neighborhood.objects.get(pk=request.data['neighborhood_id'])
        except:
            return Response({'detail': 'Invalid user_id or neighborhood_id'}, status=status.HTTP_404_NOT_FOUND)
        following = NeighborhoodFollower.objects.filter(neighborhood__id=neighborhood.id, followed_by=user_id)
        if following.exists():
            following.delete()
            followed = False
            return Response({'status': followed}, status=status.HTTP_200_OK)
        else:
            data = {'neighborhood': request.data['neighborhood_id'], 'followed_by': user_id}
            serializer = NeighborhoodFollowerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                followed = True
                return Response({'status': followed}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny,))
def get_posts(request):
    if request.method == 'POST':
        try:
            user_id = User.objects.get(pk=request.data['user_id']).id
        except:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        neighborhoods_followed = NeighborhoodFollower.objects.filter(
            followed_by=user_id).values_list('neighborhood', flat=True)

        if neighborhoods_followed.count() > 0:
            posts = Post.objects.filter(neighborhood_id__in=neighborhoods_followed).select_related(
                'neighborhood', 'user').prefetch_related('media_list', 'comments_list', 'post_likes')
            serializer = PostSerializer(posts, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            all_posts = Post.objects.all().prefetch_related('media_list', 'comments_list', 'post_likes')
            nearby_posts = [post for post in all_posts if distance(
                (request.data['latitude'], request.data['longitude']),
                (post.latitude, post.longitude)).kilometers <= 10]
            serializer = PostSerializer(nearby_posts, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
def like_post(request):
    if request.method == 'POST':
        try:
            user_id = User.objects.get(pk=request.data['user_id']).id
            post = Post.objects.get(pk=request.data['post_id'])
        except:
            return Response({'detail': 'Invalid user_id or post_id'}, status=status.HTTP_404_NOT_FOUND)
        like = PostLike.objects.filter(post__id=post.id, liked_by=user_id)
        if like.exists():
            like.delete()
            liked = False
            total_likes = PostLike.objects.filter(post__id=post.id).count()
            return Response({'status': liked, 'total_likes': total_likes}, status=status.HTTP_200_OK)
        else:
            data = {'post': request.data['post_id'], 'liked_by': user_id}
            serializer = PostLikeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                liked = True
                total_likes = PostLike.objects.filter(post__id=post.id).count()
                return Response({'status': liked, 'total_likes': total_likes}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_comment(request):
    if request.method == 'POST':
        request.data['post'] = request.data['post_id']
        del request.data['post_id']
        try:
            User.objects.get(pk=request.data['commented_by'])
        except:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Comment created successfully.'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_post_comments(request, pk):
    if request.method == 'GET':
        try:
            Post.objects.get(pk=pk)
        except:
            return Response({'detail': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)
        comments = Comment.objects.filter(post__id=pk)
        if comments.exists():
            serializer = CommentSerializer(comments, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No comments on this post'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes((AllowAny,))
def like_comment(request):
    if request.method == 'POST':
        try:
            user_id = User.objects.get(pk=request.data['user_id']).id
            comment_id = Comment.objects.get(pk=request.data['comment_id']).id
        except:
            return Response({'detail': 'Invalid user_id or comment_id'}, status=status.HTTP_404_NOT_FOUND)
        like = CommentLike.objects.filter(comment__id=comment_id, liked_by=user_id)
        if like.exists():
            like.delete()
            liked = False
            total_likes = CommentLike.objects.filter(comment__id=comment_id).count()
            return Response({'status': liked, 'total_likes': total_likes}, status=status.HTTP_200_OK)
        else:
            data = {'comment': request.data['comment_id'], 'liked_by': user_id}
            serializer = CommentLikeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                liked = True
                total_likes = CommentLike.objects.filter(comment__id=comment_id).count()
                return Response({'status': liked, 'total_likes': total_likes}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny,))
def edit_comment(request):
    if request.method == 'POST':
        try:
            comment = Comment.objects.get(pk=request.data['id'])
        except:
            return Response({'detail': 'Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        comment.comment_text = request.data['comment_text']
        comment.save()
        return Response({'detail': 'Comment updated successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
def delete_comment(request):
    if request.method == 'POST':
        try:
            comment = Comment.objects.get(pk=request.data['id'])
        except:
            return Response({'detail': 'Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        comment.delete()
        return Response({'detail': 'Comment deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
def send_connection_request(request):
    if request.method == 'POST':
        user_id, send_to_user_id, = request.data['user_id'], request.data['send_to_user_id']
        if user_id == send_to_user_id:
            return Response({'detail': 'One of the ids is invalid'}, status=status.HTTP_400_BAD_REQUEST)
        elif Connection.objects.filter(Q(user_one=user_id, user_two=send_to_user_id) |
                                       Q(user_one=send_to_user_id, user_two=user_id)).exists():
            return Response({'detail': 'Both users are already connected.'}, status=status.HTTP_400_BAD_REQUEST)
        elif ConnectionRequest.objects.filter(sent_by=user_id, sent_to=send_to_user_id).exists():
            return Response(
                {'detail': 'Connection request already sent to other user'}, status=status.HTTP_400_BAD_REQUEST)
        elif ConnectionRequest.objects.filter(sent_by=send_to_user_id, sent_to=user_id).exists():
            return Response(
                {'detail': 'Connection request is pending from other user'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = {
                'sent_by': user_id,
                'sent_to': send_to_user_id
            }
            connection_request_serializer = ConnectionRequestSerializer(data=data)
            if connection_request_serializer.is_valid():
                connection_request_serializer.save()
                return Response({'detail': 'Connection request sent'}, status=status.HTTP_200_OK)
            else:
                return Response(connection_request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny,))
def accept_connection_request(request):
    if request.method == 'POST':
        user_id, sent_by_user_id = request.data['user_id'], request.data['sent_by_user_id']
        if user_id == sent_by_user_id:
            return Response({'detail': 'One of the ids is invalid'}, status=status.HTTP_400_BAD_REQUEST)
        elif Connection.objects.filter(Q(user_one=user_id, user_two=sent_by_user_id) |
                                       Q(user_one=sent_by_user_id, user_two=user_id)).exists():
            return Response({'detail': 'Both users are already connected.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                connection_request = ConnectionRequest.objects.get(sent_by=sent_by_user_id, sent_to=user_id)
            except:
                return Response({'detail': 'Connection request does not exist'}, status=status.HTTP_404_NOT_FOUND)
            connection_serializer = ConnectionSerializer(data={'user_one': sent_by_user_id, 'user_two': user_id})
            if connection_serializer.is_valid():
                connection_serializer.save()
                connection_request.delete()
                return Response(
                    {'detail': 'Request accepted and connection created successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(connection_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_connections(request, pk):
    if request.method == 'GET':
        if not User.objects.filter(pk=pk).exists():
            return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            user_connections = Connection.objects.filter(Q(user_one=pk) | Q(user_two=pk))
            if user_connections.exists():
                serializer = ConnectionSerializer(
                    user_connections, many=True, context={'request': request, 'user': pk})
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'User has no connections'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_sent_connection_requests(request, pk):
    if request.method == 'GET':
        if not User.objects.filter(pk=pk).exists():
            return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        sent_requests = ConnectionRequest.objects.filter(sent_by=pk)
        if sent_requests.exists():
            context = {
                'request': request,
                'type': 'sent_requests'
            }
            serializer = ConnectionRequestSerializer(sent_requests, many=True, context=context)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'User has no sent requests'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_pending_connection_requests(request, pk):
    if request.method == 'GET':
        if not User.objects.filter(pk=pk).exists():
            return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        pending_requests = ConnectionRequest.objects.filter(sent_to=pk)
        if pending_requests.exists():
            context = {
                'request': request,
                'type': 'pending_requests'
            }
            serializer = ConnectionRequestSerializer(pending_requests, many=True, context=context)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'User has no pending requests'}, status=status.HTTP_200_OK)
