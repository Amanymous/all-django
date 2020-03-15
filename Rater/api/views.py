# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import viewsets,status
from rest_framework.authentication import TokenAuthentication
# from rest_framework.compat import stars
from .models import Todo,Rating
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import TodoSerializer,RatingSerializer,UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=TodoSerializer
    permission_classes = (AllowAny,)

class TodoViewSet(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True,methods=['POST'])
    def rate_todos(self,request,pk=None):
        # if stars=='stars':
        #     response={'message':'it is working'}
        #     return Response(response,status=status.HTTP_200_OK)
        # else:
        #     response={'message':'doesnot match to condition'}
        #     return Response(response,status=status.HTTP_400_BAD_REQUEST)

        if 'stars' in request.data:
            todo=Todo.objects.get(id=pk)
            stars=request.data['stars']
            user=request.user
            # user=User.objects.get(id=1)
            # print('user' ,user.username)
            try:
                rating=Rating.objects.get(user=user.id,todo=todo.id)
                rating.stars=stars
                rating.save()
                serializer=RatingSerializer(rating,many=False)
                response={'message':'updated','result':serializer.data}
                return Response(response,status=status.HTTP_200_OK)
            except:
                rating=Rating.objects.Create(user=user.id,todo=todo.id,stars=stars)
                serializer=RatingSerializer(rating,many=False)
                response={'message':'created','result':serializer.data}
                return Response(response,status=status.HTTP_200_OK)
        else:
            response={'message':'please provide the stars'}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
