from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Road
from .serializers import RoadSerializer
from rest_framework import status


class RoadListAPIView(APIView):

    def get(self, request):
        roads = Road.objects.all()
        serializer = RoadSerializer(roads, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoadSerializer(data=request.data, many=True)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors
                        , status=status.HTTP_400_BAD_REQUEST)


class RoadDetailAPIView(APIView):

    def get_obj(self, pk):
        try:
            return Road.objects.get(pk=pk)

        except Road.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        current_road = self.get_obj(pk=pk)
        serializer = RoadSerializer(current_road)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        current_road = self.get_obj(pk=pk)
        serializer = RoadSerializer(current_road, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        current_road = self.get_obj(pk=pk)
        current_road.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
