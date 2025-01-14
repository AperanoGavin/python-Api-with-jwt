
from django.urls import path , include
from Api.api_rest.views import MovieList , MovieDetails , StreamPlateformList , StreamPlateformDetails
urlpatterns = [
    path('list/' , MovieList.as_view() , name='allMovie'),
    path('<int:pk>/' , MovieDetails.as_view() , name ='detailMovie'),
    path('stream/' , StreamPlateformList.as_view() , name="streamPlat"),
    path('stream/<int:pk>/' , StreamPlateformDetails.as_view() , name="streamDet")
    
]
   