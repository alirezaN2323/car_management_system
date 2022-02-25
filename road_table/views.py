from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from road_table.models import AllNode
from road_table.serializers import AllNodeSerializer


class AllNodeListAPIView(APIView):
    def get(self, request):
        all_nodes = AllNode.objects.all()
        serializer = AllNodeSerializer(all_nodes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AllNodeSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllNodeDetailAPIView(APIView):
    def get_obj(self, pk):
        try:
            return AllNode.objects.get(pk=pk)
        except AllNode.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        current_node = self.get_obj(pk=pk)
        serializer = AllNodeSerializer(current_node)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        current_node = self.get_obj(pk=pk)
        serializer = AllNodeSerializer(current_node, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        current_node = self.get_obj(pk=pk)
        current_node.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
