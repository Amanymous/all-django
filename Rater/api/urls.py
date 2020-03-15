
from django.urls import path
# ye api ka urls file ha is models ki specification likhy gy
# isky account bany gy python3 manage.py createsuperuser
from rest_framework import routers
from django.conf.urls import include
# views.py ki file sy liya gya ha
from .views import TodoViewSet,RatingViewSet,UserViewSet

router=routers.DefaultRouter()
router.register('todos',TodoViewSet)#from views.py
router.register('ratings',RatingViewSet)#from views.py
router.register('users',UserViewSet)
urlpatterns = [
    path('', include(router.urls)),#ye urls ky liye jo model ky model ma class bany gi
]
