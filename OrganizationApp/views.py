from django.shortcuts import render
from rest_framework import permissions,generics,viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny,IsAdminUser

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]
    
class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class SubOrganizationList(generics.ListCreateAPIView):
    queryset = SubOrganization.objects.all()
    serializer_class = SubOrgSerializer
    permission_classes = [IsAdminUser]
    
class SubOrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubOrganization.objects.all()
    serializer_class = SubOrgSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    
class DivList(generics.ListCreateAPIView):
    queryset = Division.objects.all()
    serializer_class = DivSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class DivDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Division.objects.all()
    serializer_class = DivSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SubdivList(generics.ListCreateAPIView):
    queryset = SubDivision.objects.all()
    serializer_class = SubdivSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class SubdivDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubDivision.objects.all()
    serializer_class = SubdivSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EmpList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
    permission_classes = [AllowAny]

class EmpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
    permission_classes = [AllowAny]