from rareapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    uid = request.data['uid']
    user = User.objects.filter(uid=uid).first()

    if user is not None:
        data = {
            'firstName': user.first_name,
            'lastName': user.last_name,
            'bio': user.bio,
            'profileImageUrl': user.profile_image_url,
            'email': user.email,
            'created_on': user.created_on,
            'active': user.active,
            'isStaff': user.is_staff,
        }
        return Response(data)
    else:
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    user = User.objects.create(
        profile_image_url=request.data['profileImageUrl'],
        bio=request.data['bio'],
        uid=request.data['uid'],
        first_name=request.data['firstName'],
        last_name=request.data['lastName'],
        email=request.data['email']
    )

    data = {
        'id': user.id,
        'uid': user.uid,
        'bio': user.bio,
        'firstName': user.first_name,
        'lastName': user.last_name,
        'profileImageUrl': user.profile_image_url
    }

    return Response(data)
