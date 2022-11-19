from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from dj_rest_auth.views import LogoutView

from item.models import Item
from item.serializers import ItemSerializer


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class TestAuthView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        return Response("Hello {0}!".format(request.user))
    
    def post(self, request, format=None):
        return Response("Hello {0}! Posted!".format(request.user))


class LogoutViewEx(LogoutView):
    authentication_classes = (authentication.TokenAuthentication,)
    
class ItemReturnAllView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
class ItemReturnView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def get(self, request, pk, format=None):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return HttpResponse(status=404)
        
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)
    