from os.path import splitext
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from urllib.request import urlopen

from credential.models import UserDetails

from .serializer import *
from .models import *


@api_view(['POST'])
@permission_classes((AllowAny,))
def post_short(request):
    if request.method == 'POST':
        video = request.FILES['video']
        valid_video_formats = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.m4v', '.mpg', '.mpeg',
                               '.3gp', '.3g2', '.ts', '.vob']
        if splitext(video.name)[1] in valid_video_formats:
            data = request.POST.copy()
            data['user'] = data['user_id']
            del data['user_id']
            try:
                user_details = UserDetails.objects.get(user=data['user'])
            except:
                return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
            data['username'] = user_details.user.username
            image = user_details.profile_image
            if image == '':
                data['profile_photo'] = ''
            else:
                try:
                    urlopen(str(image))
                    data['profile_photo'] = str(image)
                except:
                    data['profile_photo'] = request.build_absolute_uri(image.url)
            data['video'] = video
            serializer = ShortSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': 'Short has been posted successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Invalid video format'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_shorts(request):
    if request.method == 'GET':
        all_shorts = Short.objects.all()
        serializer = ShortSerializer(all_shorts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
