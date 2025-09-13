from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSignupSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from .models import GlassesLocation
from .serializers import GlassesLocationSerializer
from django.http import HttpResponse

# Signup API
@api_view(["POST"])
def signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login API
@api_view(["POST"])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# POST - update location
class UpdateLocationView(generics.CreateAPIView):
    serializer_class = GlassesLocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# GET - fetch latest location
class GetLocationView(generics.ListAPIView):
    serializer_class = GlassesLocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        glasses_id = self.request.query_params.get("glasses_id")
        if glasses_id:
            return GlassesLocation.objects.filter(user=self.request.user, glasses_id=glasses_id).order_by('-timestamp')[:1]
        return GlassesLocation.objects.filter(user=self.request.user).order_by('-timestamp')

# smartglasses/views.py

def home(request):
    return HttpResponse("Welcome to the homepage!")

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'signup':reverse('signup', request=request,format=format),
        'login':reverse('login', request=request,format=format),
        'get-location':reverse('get-location', request=request,format=format),
        'update-location':reverse('update-location', request=request,format=format)

    })