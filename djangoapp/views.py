from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from .models import Assets
from .serializers import AssetsSerializer


@api_view(['GET'])
def getDataUser(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('User successfully deleted!')

@api_view(['GET'])
def getDataAssets(request):
    assets = Assets.objects.all()
    serializer = AssetsSerializer(assets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAssets(request, pk):
    assets = Assets.objects.get(id=pk)
    serializer = AssetsSerializer(assets, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addAssets(request):
    serializer = AssetsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateAssets(request, pk):
    assets = Assets.objects.get(id=pk)
    serializer = AssetsSerializer(instance=assets, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteAssets(request, pk):
    assets = Assets.objects.get(id=pk)
    assets.delete()
    return Response('Assets successfully deleted!')

@api_view(['GET'])
def getAssetsUser(request, pk):
    user = User.objects.get(id=pk)
    assets = Assets.objects.filter(user=user)
    serializer = AssetsSerializer(assets, many=True)
    return Response(serializer.data)