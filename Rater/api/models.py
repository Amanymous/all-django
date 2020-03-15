from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Todo(models.Model):
    title=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    description=models.CharField(max_length=500)

    def no_of_ratings(self):
        ratings=Rating.objects.filter(todo=self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings=Rating.objects.filter(todo=self)
        for rating in ratings:
            sum+=rating.stars
        if len(ratings)>0:
            return sum/len(ratings)
        else:
            return 0

class Rating(models.Model):
    todo=models.ForeignKey(Todo,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    class Meta:
        unique_together=(('user','todo'),)
        index_together=(('user','todo'))
# python3 manage.py makemigration
# python3 manage.py migrate
# phir admin ma jaky model register karna ha

# Create your models here.
# or token leny ky liye settings.py ma install apps='rest_framework.authtoken',
# or phir isko migrate bi karna ha
# 	48459676de657fd734ace393472c01ab62910fed token
# 48459676de657fd734ace393472c01ab62910fed postman token get kiya ha