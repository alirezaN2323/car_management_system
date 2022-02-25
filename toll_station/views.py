from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from toll_station.models import TollStation
from toll_station.serializers import TollStationSerializer
from rest_framework.views import APIView


class TollStationListAPIView(APIView):
    def get(self, request):
        toll_stations = TollStation.objects.all()
        serializer = TollStationSerializer(toll_stations, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TollStationSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class TollStationDetailAPIView(APIView):
    def get_obj(self, pk):
        try:
            return TollStation.objects.get(pk=pk)
        except TollStation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        current_toll_station = self.get_obj(pk=pk)
        serializer = TollStationSerializer(current_toll_station)
        return Response(serializer.data)

    def put(self, request, pk):
        current_toll_station = self.get_obj(pk=pk)

        serializer = TollStationSerializer(instance=current_toll_station,
                                           data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        current_toll_station = self.get_obj(pk=pk)

        current_toll_station.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

