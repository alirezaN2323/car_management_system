from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from vehicle.models import Vehicle
from owner.models import Owner
from owner.serializers import OwnerSerializer


def create_vehicles(vehicle_data, car_owner):
    for vehicle in vehicle_data:
        current_vehicle = Vehicle(
            type="S" if vehicle['type'] == "small" else "B",
            color=vehicle['color'],
            owner=car_owner,
            load_valume=vehicle.get(
                'load_valume'),
            length=vehicle['length'],
            input_id=vehicle['id'])

        current_vehicle.save()


class OwnerListAPIView(APIView):

    def get(self, request):
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        if type(data) == list:
            serializers_list = list()

            for item in data:
                own_vehicles = None

                if item['ownerCar']:
                    own_vehicles = item.pop('ownerCar')

                serializer = OwnerSerializer(data=item)

                if serializer.is_valid():
                    new_owner = serializer.save()
                    serializers_list.append(serializer.data)

                    if own_vehicles:
                        create_vehicles(vehicle_data=own_vehicles,
                                        car_owner=new_owner)
                else:
                    return Response(serializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)

            return Response(serializers_list,
                            status=status.HTTP_201_CREATED)

        elif type(data) == dict:
            own_vehicles = None

            if data['ownerCar']:
                own_vehicles = data.pop('ownerCar')

            serializer = OwnerSerializer(data=data)
            if serializer.is_valid():
                new_owner = serializer.save()
                if own_vehicles:
                    create_vehicles(vehicle_data=own_vehicles,
                                    car_owner=new_owner)

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class OwnerDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Owner.objects.get(pk=pk)

        except Owner.DoesNotExist:
            raise Http404

    def get(self, request, pk):

        current_owner = self.get_object(pk=pk)
        serializer = OwnerSerializer(current_owner)

        return Response(serializer, status=status.HTTP_200_OK)

    def put(self, request, pk):
        current_owner = self.get_object(pk=pk)

        serializer = OwnerSerializer(current_owner, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        current_owner = self.get_object(pk=pk)
        current_owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
