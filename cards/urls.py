from django.urls import path

from cards import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('play/', views.StartCardsGame.as_view(), name='start_card_game'),
    path('reset/', views.ResetCardsGame.as_view(), name='reset_card_game'),
    path('count/', views.CountCards.as_view(), name='count_card_details'),
    path('deal/', views.DealCards.as_view(), name='deal_card_details'),
]