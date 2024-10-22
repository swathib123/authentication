from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ManagerSerializer
from .serializers import LoginSerializer

@api_view(['POST'])
def register_manager(request):
    serializer = ManagerSerializer(data=request.data)
    if serializer.is_valid():
        manager = serializer.save()
        return Response({'id': manager.id, 'username': manager.username}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login_manager(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        return Response({
            'message': 'Login successful',
            'user': {
                'username': user.username,
                'email': user.email,
                
            }
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
