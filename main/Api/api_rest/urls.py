
from django.urls import path , include
from Api.api_rest.views import movie_list , movie_details
urlpatterns = [
    path('list/' , movie_list , name='allMovie'),
    path('<int:pk>/' , movie_details , name ='detailMovie')
    
]
   