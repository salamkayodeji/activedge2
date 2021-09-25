from django.shortcuts import render, redirect
from .models import Stock
from .serializers import StockSerializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'pk'


class StockHtmlList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'activetest/home.html'

    def get(self, request):
        queryset = Stock.objects.all()
        return Response({'stock': queryset})
    
class StockHtmlDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'activetest/detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(Stock, pk=pk)
        serializer = StockSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(Stock, pk=pk)
        serializer = StockSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('home')