# TODO: Implement betting, lists of victory, defeat, tie, and bust messages to randomize.

import random
import time

cards = [{'name': 'A\u2663', 'value': 11}, {'name': '2\u2663', 'value': 2}, {'name': '3\u2663', 'value': 3}, {'name': '4\u2663', 'value': 4}, {'name': '5\u2663', 'value': 5}, {'name': '6\u2663', 'value': 6}, {'name': '7\u2663', 'value': 7}, {'name': '8\u2663', 'value': 8}, {'name': '9\u2663', 'value': 9}, {'name': '10\u2663', 'value': 10}, {'name': 'J\u2663', 'value': 10}, {'name': 'Q\u2663', 'value': 10}, {'name': 'K\u2663', 'value': 10}, {'name': 'A\u2665', 'value': 11}, {'name': '2\u2665', 'value': 2}, {'name': '3\u2665', 'value': 3}, {'name': '4\u2665', 'value': 4}, {'name': '5\u2665', 'value': 5}, {'name': '6\u2665', 'value': 6}, {'name': '7\u2665', 'value': 7}, {'name': '8\u2665', 'value': 8}, {'name': '9\u2665', 'value': 9}, {'name': '10\u2665', 'value': 10}, {'name': 'J\u2665', 'value': 10}, {'name': 'Q\u2665', 'value': 10}, {'name': 'K\u2665', 'value': 10}, {
    'name': 'A\u2660', 'value': 11}, {'name': '2\u2660', 'value': 2}, {'name': '3\u2660', 'value': 3}, {'name': '4\u2660', 'value': 4}, {'name': '5\u2660', 'value': 5}, {'name': '6\u2660', 'value': 6}, {'name': '7\u2660', 'value': 7}, {'name': '8\u2660', 'value': 8}, {'name': '9\u2660', 'value': 9}, {'name': '10\u2660', 'value': 10}, {'name': 'J\u2660', 'value': 10}, {'name': 'Q\u2660', 'value': 10}, {'name': 'K\u2660', 'value': 10}, {'name': 'A\u2666', 'value': 11}, {'name': '2\u2666', 'value': 2}, {'name': '3\u2666', 'value': 3}, {'name': '4\u2666', 'value': 4}, {'name': '5\u2666', 'value': 5}, {'name': '6\u2666', 'value': 6}, {'name': '7\u2666', 'value': 7}, {'name': '8\u2666', 'value': 8}, {'name': '9\u2666', 'value': 9}, {'name': '10\u2666', 'value': 10}, {'name': 'J\u2666', 'value': 10}, {'name': 'Q\u2666', 'value': 10}, {'name': 'K\u2666', 'value': 10}]


def add_cards(hand):
    """Returns the highest value of a hand without going over 21."""
    total = 0
    aces = 0
    for card in hand:
        total += card["value"]
        if card["value"] == 11:
            aces += 1
    if total > 21 and aces != 0:
        for _i in range(aces):
            total = 0
            ace_dropped = False
            for card in hand:
                if card["value"] == 11 and not ace_dropped:
                    card["value"] = 1
                total += card["value"]
            if total < 21:
                return total
    return total


def play_again():
    """
    Checks to see if a player wants to play again.

    Returns Boolean
    """
    while True:
        answer = input("Do you dare brave Saddam's wrath again? [y/n]")
        try:
            answer = answer.lower()
        except:
            print("Sorry, I don't understand that command.")
            continue
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Sorry, I don't understand that command.")
            continue


def goodbye():
    print('Thank you for playing. Goodbye.')


print("$" * 40)
print("Welcome to Saddam Hussein's Blackjack!\nPrepare your anus, infidel!")
print("$" * 40)
while True:
    deck = cards[:]
    player_hand = []
    dealer_hand = []
    player_total = 0
    dealer_total = 0
    player_charlie = False
    dealer_charlie = False
    player_bust = False
    dealer_bust = False

    def deal_card(hand, deck):
        to_deal = random.randrange(0, len(deck))
        hand.append(deck[to_deal])
        deck.remove(deck[to_deal])
    for i in range(2):
        deal_card(player_hand, deck)
        deal_card(dealer_hand, deck)
    while True:
        print("*" * 40)
        print('Your hand:', end=" ")
        for card in player_hand:
            print(card["name"], end=" ")
        print()
        print(f"Saddam's hand: [X] {dealer_hand[1]['name']}")
        player_total = add_cards(player_hand)
        if len(player_hand) == 2 and player_total == 21:
            print("BLACKJACK!!!")
            time.sleep(1)
            print("Can this be the end for Saddam?...")
            time.sleep(1)
            print("Saddam's hand:", end=" ")
            for card in dealer_hand:
                print(card["name"], end=" ")
            print()
            dealer_total = add_cards(dealer_hand)
            time.sleep(1)
            if player_total > dealer_total:
                print('You win! Saddam is your lady boy slave!')
                if play_again():
                    continue
                else:
                    break
            elif player_total == dealer_total:
                print("Double blackjack! No one wins this hand.")
                if play_again():
                    continue
                else:
                    break
        hit_stay = input('Would you like to hit["h"] or stay["s"]? ')
        if hit_stay == "s":
            player_total = add_cards(player_hand)
            break
        elif hit_stay == "h":
            deal_card(player_hand, deck)
            player_total = add_cards(player_hand)
            if player_total > 21:
                print("*" * 40)
                print('Your hand:', end=" ")
                for card in player_hand:
                    print(card["name"], end=" ")
                print()
                player_bust = True
                break
            if len(player_hand) == 5:
                charlie = True
                break
            else:
                continue
        else:
            if hit_stay != "h" or hit_stay != "s":
                print("Sorry, I don't recognize that command.")

    if player_charlie:
        print("You escaped Saddam's Blackjack Dungeon!")
        if play_again():
            continue
        else:
            break
    elif player_bust:
        print("BUST!!! Saddam will have your eyes for this!")
        if play_again():
            continue
        else:
            break
    else:
        # dealer's turn
        print("#" * 40)
        print("Saddam's turn!")
        print("#" * 40)
        while True:
            print("*" * 40)
            print('Your hand:', end=" ")
            for card in player_hand:
                print(card["name"], end=" ")
            print()
            print("Saddam's hand:", end=" ")
            for card in dealer_hand:
                print(card["name"], end=" ")
            print()
            dealer_total = add_cards(dealer_hand)
            time.sleep(1)
            if dealer_total > 21:
                dealer_bust = True
                break
            elif len(dealer_hand) == 5:
                dealer_charlie = True
                break
            elif dealer_total < player_total:
                time.sleep(1)
                print('Saddam hits.')
                time.sleep(1)
                deal_card(dealer_hand, deck)
            elif dealer_total >= player_total:
                break

        if dealer_bust:
            print('Saddam busts!!! You teabag him in victory!')
            if play_again():
                continue
            else:
                goodbye()
                break
        elif dealer_charlie:
            print(
                "Saddam's stamina proves too great. You lose. The universe weeps for your fate.")
            if play_again():
                continue
            else:
                break
        elif dealer_total == player_total:
            print('You reach a stalemate with Saddam. The fates sneeze in your mouth.')
            if play_again():
                continue
            else:
                goodbye()
                break
        elif dealer_total > player_total:
            print(
                'You lose. Saddam ties you down and sticks his tongue in your nose! Too bad...')
            if play_again():
                continue
            else:
                goodbye()
                break
        else:
            print("You are victorious! Saddam's scalp adorns your belt forevermore.")
            if play_again():
                continue
            else:
                goodbye()
                break
    break
