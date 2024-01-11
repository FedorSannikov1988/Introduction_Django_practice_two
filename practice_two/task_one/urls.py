from .views import heads_or_tails, heads_or_tails_statistics
from django.urls import path


urlpatterns = [

    path('heads_or_tails',
         heads_or_tails,
         name='heads_or_tails'),

    path('heads_or_tails_statistics/<int:number_throws>/',
         heads_or_tails_statistics,
         name='heads_or_tails_statistics'),

]
