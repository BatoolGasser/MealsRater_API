from rest_framework import viewsets, status
from .models import Rating, Meal
from .serializers import MealSerializer, RatingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import request
from django.contrib.auth.models import User


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(detail=True, methods=['post'])
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update
            '''
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(username=username)
            try:
                rating = Rating.objects.get(user=user.id, meal=meal.id)  # specific rate
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)

                json = {
                    'message': 'Meal Rate updated',
                    'result': serializer.data
                }

                return Response(json)

            except:
                # create , if the rate not exist
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Meal Rate Created',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_201_CREATED)


        else:
            json = {
                'message': 'Stars Not Provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
