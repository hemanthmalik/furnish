from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from . import serializers as user_serializers

User = get_user_model()

@api_view(['POST'])
@parser_classes((JSONParser,))
def register(request):
    data = request.data
    serializer = user_serializers.UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    mobileNo = data.pop('mobileNo')
    password = data.pop('password')
    User.objects.create_user(mobileNo, password, **data)
    response = {'success': True, 'detail': 'Registration Successful.'}
    
    return Response(response)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id,
            'mobileNo': user.mobileNo,
            'token': token.key,
        })


class SecuredTestAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return Response({'success': True, "detail": "you are an authenticated user."})

    