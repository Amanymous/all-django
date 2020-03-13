from django.urls import path,include
from rest_framework import routers
from .views import BookViewSet
# from . import views
# from .views import Another 1st

router=routers.DefaultRouter()
router.register('books',BookViewSet)
urlpatterns = [

    # path('firstfunction',views.first),
    #1st path('another',Another.as_view()),#another class
    # path('first',views.first)
    path('',include(router.urls))
]
#is ma urls.py/demo ky sary fuction use horhy hain