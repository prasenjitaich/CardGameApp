# CardGameApp

1. Assuming a standard deck (52 cards of 4 suits: ♣ Clubs, ♦ Diamonds, ♥ Hearts, ♠ Spades).
2. Press a "Deal" button to deal 5 random cards.
3. Pressing the button again should deal 5 unique, random cards. Within the same game, you should never get the same cards again that you got in the past (just like a physical deck).
4. API for a card counter which shows how many cards are dealt/left.
5. API to reset the game.
6. API to show the game is over.
7. API for win/lose. If there is an ace in the last draw, display You Win, otherwise display You Lose, Sucker.
8. Unit tests.

### Getting started

Create a python virtual environment using below command.

**python3 -m venv virtual-env**

Activate the environment.

**source virtual-env/bin/activate**

Install dependencies.

**pip install -r requirements.txt**


**python manage.py migrate**

Run this command and your django app should be running on port 8000

**python manage.py runserver**
