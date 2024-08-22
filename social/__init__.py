from urllib.request import urlopen


def retrieve_user_data(user, request):
    image = user.user_detail.profile_image
    if image == '':
        profile_image = ''
    else:
        try:
            urlopen(str(image))
            profile_image = str(image)
        except Exception:
            profile_image = request.build_absolute_uri(image.url)
    user_data = {
        'id': user.id,
        'username': user.username,
        'profile_image': profile_image,
    }
    return user_data
