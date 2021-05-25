from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cards.views import StartCardsGame, ResetCardsGame, CountCards, DealCards


class TestUrls(SimpleTestCase):

    def test_start_card_game_url_is_resolved(self):
        url = reverse("start_card_game")
        self.assertEquals(resolve(url).func.view_class, StartCardsGame)

    def test_reset_card_game_url_is_resolved(self):
        url = reverse("reset_card_game")
        self.assertEquals(resolve(url).func.view_class, ResetCardsGame)

    def test_count_card_details_url_is_resolved(self):
        url = reverse("count_card_details")
        self.assertEquals(resolve(url).func.view_class, CountCards)

    def test_deal_card_details_url_is_resolved(self):
        url = reverse("deal_card_details")
        self.assertEquals(resolve(url).func.view_class, DealCards)
