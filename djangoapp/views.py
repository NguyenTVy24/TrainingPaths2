from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from .models import Assets
from .serializers import AssetsSerializer



class User_view(APIView):
    @api_view(['GET'])
    def getData(request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    @api_view(['GET'])
    def getId(request, pk):
        users = User.objects.get(id=pk)
        serializer = UserSerializer(users, many=False)
        return Response(serializer.data)
    @api_view(['POST'])
    def add(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['PUT'])
    def update(request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    @api_view(['DELETE'])
    def delete(request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response('User successfully deleted!')
    
class Assets_views(APIView):
    @api_view(['GET'])
    def getData(request):
        assets = Assets.objects.all()
        serializer = AssetsSerializer(assets, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def getId(request, pk):
        assets = Assets.objects.get(id=pk)
        serializer = AssetsSerializer(assets, many=False)
        return Response(serializer.data)

    @api_view(['POST'])
    def add(request):
        serializer = AssetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['PUT'])
    def update(request, pk):
        assets = Assets.objects.get(id=pk)
        serializer = AssetsSerializer(instance=assets, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['DELETE'])
    def delete(request, pk):
        assets = Assets.objects.get(id=pk)
        assets.delete()
        return Response('Assets successfully deleted!')

    @api_view(['GET'])
    def getFollowUser(request, pk):
        user = User.objects.get(id=pk)
        assets = Assets.objects.filter(user=user)
        serializer = AssetsSerializer(assets, many=True)
        return Response(serializer.data)