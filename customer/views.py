from rest_framework import views, response, status, viewsets
from .serializers import CustomerSerializer
from .models import Customer


class CustomerListCreateAPIView(views.APIView):
    serializer_class = CustomerSerializer

    def get(self, request):
        queryset = Customer.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerDetailView(views.APIView):
    serializer_class = CustomerSerializer

    def get(self, request, pk):
        instance = Customer.objects.get(pk=pk)
        serializer = self.serializer_class(instance=instance)
        return response.Response(serializer.data)

    def patch(self, request, pk):
        instance = Customer.objects.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def delete(self, request, pk):
        try:
            instance = Customer.objects.get(pk=pk)
            instance.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist:
            return response.Response({'message': 'customer not found'})
