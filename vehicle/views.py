from django.contrib.gis.geos import Point
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from owner.models import Owner
from road.models import Road
from road_table.models import AllNode
from toll_station.models import TollStation
from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer


class VehicleListAPIView(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(instance=vehicles, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleDetailAPIView(APIView):
    def get_obj(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        current_vehicle = self.get_obj(pk=pk)
        serializer = VehicleSerializer(instance=current_vehicle)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        current_vehicle = self.get_obj(pk=pk)
        serializer = VehicleSerializer(current_vehicle,
                                       data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        current_vehicle = self.get_obj(pk=pk)
        current_vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_vehicles_with_old_owners(request):
    current_age = request.data.get('age', 70)

    vehicles = Vehicle.objects.filter(owner__age__gt=current_age)
    serializer = VehicleSerializer(instance=vehicles, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_vehicles_with_current_colors(request):
    data = request.data.get('colors')

    colors = data.split(',') if data else ['blue', 'red']
    vehicles = Vehicle.objects.filter(color__in=colors)
    serializer = VehicleSerializer(instance=vehicles, many=True)
    return Response(serializer.data)


# Got Wrong Result
def get_misfeasance_heavy_vehicles():
    AllNode.objects.filter(location__in=
                           [road.geom for road in Road.objects.filter(
                               width__lt=600)]).filter(
        car__input_id__in=[heavy_vehicle.input_id for heavy_vehicle in
                           Vehicle.objects.all()]
    )


@api_view(['GET'])
def get_misfeasance_cost_of_each_vehicle(request):
    sum_of_misfeasance_vehicles = dict()
    sum_of_misfeasance_owners = dict()
    all_data = list()

    for current_vehicle in Vehicle.objects.all():
        sum_of_misfeasance_vehicles.update({current_vehicle.id: 0})
        for node in current_vehicle.all_nodes.filter(location__in=
                                                     [toll_station.location for
                                                      toll_station in
                                                      TollStation.objects.all()]):
            sum_of_misfeasance_vehicles[
                current_vehicle.id] += TollStation.objects.get(
                location=node.location).toll_per_cross
        if current_vehicle.type == 'B':
            sum_of_misfeasance_vehicles[current_vehicle.id] += (
                    current_vehicle.load_valume * 300)

    all_data.append(sum_of_misfeasance_vehicles)

    for owner in Owner.objects.all():
        sum_of_misfeasance_owners.update({owner.name: 0})

        for owner_vehicle in owner.vehicles.all():
            sum_of_misfeasance_owners[owner.name] += \
                sum_of_misfeasance_vehicles[owner_vehicle.id]

    all_data.append(sum_of_misfeasance_owners)

    return Response(all_data)


@api_view(['GET'])
def get_guilty_heavy_vehicles(request):
    all_data = list()
    for node in AllNode.objects.filter(car__type='B'):
        data = Road.objects.filter(width__lt=20, geom__contains=node.location)
        if data:
            all_data.append({"Car id": node.car.id, "Date time": node.date,
                             "street": (item.id,
                                        item.name)}
                            for item in data)

    return Response(all_data)


@api_view(['GET', 'POST'])
def get_general_vehicles_with_600_meters_distance(request):
    all_data = list()
    toll_station_one = TollStation.objects.get(name='عوراضی 1')

    for node in AllNode.objects.filter(car__type='S'):
        if node.location.distance(toll_station_one.location) == 600:
            all_data.append({"car id": node.car.id,
                             "car location ": node.location})

    return Response(all_data)
