# rest framework
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

# base
from apps.base.api import GeneralListApiView

# serializer
from apps.products.api.serializers.product_serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk == None:
            return self.serializer_class().Meta.model.objects.filter(state=True)
        return self.serializer_class().Meta.model.objects.filter(pk=pk, state=True).first()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'product has been created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = self.get_queryset(pk)

        if product:
            product.state = False
            product.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'no existe el producto'}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(data=product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'no existe el producto'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        if request.data['image'] is None:
            request.data['image'] = ''

        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if product_serializer.is_valid():
                product_serializer.save()
                return Response(data=product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'no existe el producto'}, status=status.HTTP_404_NOT_FOUND)


class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.serializer_class().Meta.model.objects.filter(state=True)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self, pk=None):
        if pk == None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(pk=pk, state=True).first()
 
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()

        if product:
            product.state = False
            product.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'no existe el producto'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(data=product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'no existe el producto'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk=None):
        if request.data['image'] is None:
            request.data['image'] = ''

        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if product_serializer.is_valid():
                product_serializer.save()
                return Response(data=product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'no existe el producto'}, status=status.HTTP_404_NOT_FOUND)


class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.serializer_class().Meta.model.objects.filter(state=True)

    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()

        if product:
            product.state = False
            product.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'no existe el producto'}, status=status.HTTP_404_NOT_FOUND)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state=True).filter(pk=pk).first()
    
    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(data=product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'no existe el producto'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if product_serializer.is_valid():
                product_serializer.save()
                return Response(data=product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'no existe el producto'}, status=status.HTTP_404_NOT_FOUND)
