from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from bills.serializers import CategorySerializer, BillSerializer
from bills.models import Category, Bill


class CategoryAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Category.objects.get(pk=id)
            serializer = CategorySerializer(item)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return Response(status=404)
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CategoryAPIListView(APIView):

    def get(self, request, format=None):
        items = Category.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = CategorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BillAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Bill.objects.get(pk=id)
            serializer = BillSerializer(item)
            return Response(serializer.data)
        except Bill.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Bill.objects.get(pk=id)
        except Bill.DoesNotExist:
            return Response(status=404)
        serializer = BillSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Bill.objects.get(pk=id)
        except Bill.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class BillAPIListView(APIView):

    def get(self, request, format=None):
        items = Bill.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = BillSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
