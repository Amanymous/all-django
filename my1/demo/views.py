# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from .models import Book 1st 


class BookViewSet(viewsets.ModelViewSet):
    serializer_class=BookSerializer
    queryset=Book.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

# class Another(View):1st

#     book=Book.objects.get(id=1)
#     output=f"we have {book.title} books in database and {book.id}"
#     # for book in books:
#         # output+=f"we have {book.title} books in database and {book.id}"

#     def get(self,request):
#         return HttpResponse(self.output)

# def first(request):
#     return HttpResponse('my first messge from views')

# def first(request):
#     books=Book.objects.all()
#     return render(request,'first_temp.html',{'books':books})



