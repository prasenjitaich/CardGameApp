import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import constants
from response_utils import ApiResponse, get_error_message
from utils import Deck
from users.models import User

logger = logging.getLogger('django')


class StartCardsGame(APIView):
    """
    Class is used for start the game.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Function is used to start the game.
        :param request: request header with required info.
        :return: success message/failure messages.
        """
        user = request.user
        if user.deck_object is None:
            deck = Deck()
            deck.shuffle()
            user.deck_object = deck
            user.save()
        deck = user.deck_object
        data = str(deck).split(',')
        api_response = ApiResponse(status=1, data=data, message=constants.PLAY_GAME_SUCCESS,
                                   http_status=status.HTTP_200_OK)
        return api_response.create_response()


class CountCards(APIView):
    """
    Class is used for Count left cards in this deck/dealt cards from this deck.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Function is used to count left cards in this deck/dealt cards from this deck.
        :param request: request header with required info.
        :return: Count left cards in this deck/dealt cards from this deck.
        """
        user = request.user
        deck = user.deck_object
        if deck:
            count_dict = dict()
            count_dict['left_cards'] = deck.count_left_cards()
            count_dict['dealt_cards'] = deck.count_dealt_cards()
            user.deck_object = deck
            user.save()
            data = count_dict
            api_response = ApiResponse(status=1, data=data, message=constants.COUNT_GET_SUCCESS,
                                       http_status=status.HTTP_200_OK)
            return api_response.create_response()
        api_response = ApiResponse(status=0, message=constants.COUNT_GET_FAIL,
                                   http_status=status.HTTP_400_BAD_REQUEST)
        return api_response.create_response()


class DealCards(APIView):
    """
    Class is used for Deal cards from the deck.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Function is used for Deal cards from the deck from the deck.
        :param request: request header with required info.
        :return: for Deal cards from the deck.
        """
        user = request.user
        deck = user.deck_object
        if deck:
            if deck.count_left_cards() >= constants.HAND_CARD:
                deck.move_cards(constants.HAND_CARD)
                hand_cards = deck.hand_cards()
                user.deck_object = deck
                user.save()
                api_response = ApiResponse(status=1, data=hand_cards, message=constants.DEAL_GET_SUCCESS,
                                           http_status=status.HTTP_200_OK)
                return api_response.create_response()
            result = deck.result()
            if result:
                message = constants.WIN + " " + constants.GAME_OVER
            else:
                message = constants.LOSE + " " + constants.GAME_OVER
            remaining_cards = str(deck).split(',')
            user.deck_object = None
            user.save()
            api_response = ApiResponse(status=1, data=remaining_cards, message=message,
                                       http_status=status.HTTP_200_OK)
            return api_response.create_response()
        api_response = ApiResponse(status=0, message=constants.DEAL_GET_FAIL,
                                   http_status=status.HTTP_400_BAD_REQUEST)
        return api_response.create_response()


class ResetCardsGame(APIView):
    """
    Class is used for reset the game.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Function is used to reset the game.
        :param request: request header with required info.
        :return: success message/failure messages.
        """
        user = request.user
        deck = Deck()
        deck.shuffle()
        user.deck_object = deck
        user.save()
        api_response = ApiResponse(status=1, message=constants.RESET_GAME_SUCCESS,
                                   http_status=status.HTTP_200_OK)
        return api_response.create_response()
