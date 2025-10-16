from rest_framework import generics, permissions
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

class RegisterView (generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        },
        status=status.HTTP_201_CREATED
                        )