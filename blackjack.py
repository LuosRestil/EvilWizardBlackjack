# TODO: Implement betting, lists of victory, defeat, tie, and bust messages to randomize.

import random
import time

cards = [{'name': 'A\u2663', 'value': 11}, {'name': '2\u2663', 'value': 2}, {'name': '3\u2663', 'value': 3}, {'name': '4\u2663', 'value': 4}, {'name': '5\u2663', 'value': 5}, {'name': '6\u2663', 'value': 6}, {'name': '7\u2663', 'value': 7}, {'name': '8\u2663', 'value': 8}, {'name': '9\u2663', 'value': 9}, {'name': '10\u2663', 'value': 10}, {'name': 'J\u2663', 'value': 10}, {'name': 'Q\u2663', 'value': 10}, {'name': 'K\u2663', 'value': 10}, {'name': 'A\u2665', 'value': 11}, {'name': '2\u2665', 'value': 2}, {'name': '3\u2665', 'value': 3}, {'name': '4\u2665', 'value': 4}, {'name': '5\u2665', 'value': 5}, {'name': '6\u2665', 'value': 6}, {'name': '7\u2665', 'value': 7}, {'name': '8\u2665', 'value': 8}, {'name': '9\u2665', 'value': 9}, {'name': '10\u2665', 'value': 10}, {'name': 'J\u2665', 'value': 10}, {'name': 'Q\u2665', 'value': 10}, {'name': 'K\u2665', 'value': 10}, {
    'name': 'A\u2660', 'value': 11}, {'name': '2\u2660', 'value': 2}, {'name': '3\u2660', 'value': 3}, {'name': '4\u2660', 'value': 4}, {'name': '5\u2660', 'value': 5}, {'name': '6\u2660', 'value': 6}, {'name': '7\u2660', 'value': 7}, {'name': '8\u2660', 'value': 8}, {'name': '9\u2660', 'value': 9}, {'name': '10\u2660', 'value': 10}, {'name': 'J\u2660', 'value': 10}, {'name': 'Q\u2660', 'value': 10}, {'name': 'K\u2660', 'value': 10}, {'name': 'A\u2666', 'value': 11}, {'name': '2\u2666', 'value': 2}, {'name': '3\u2666', 'value': 3}, {'name': '4\u2666', 'value': 4}, {'name': '5\u2666', 'value': 5}, {'name': '6\u2666', 'value': 6}, {'name': '7\u2666', 'value': 7}, {'name': '8\u2666', 'value': 8}, {'name': '9\u2666', 'value': 9}, {'name': '10\u2666', 'value': 10}, {'name': 'J\u2666', 'value': 10}, {'name': 'Q\u2666', 'value': 10}, {'name': 'K\u2666', 'value': 10}]

# TODO add messages for randomized display
victory_messages = ['You win! The Evil Wizard bows to you, defeated!', 'Victory is yours! You yank a hair out of the Evil Wizard\'s beard.', 'You win! A fanfare of trumpets flourishes around you and the Wizard withers in shame.', 'You win! The Wizard shrinks in your estimation.', 'You are victorious! You step on the Evil Wizard\'s toes.', 'You win! The Evil Wizard looks sad. Did you just catch a momentary glimpse of his lost humanity?', 'You win! The sound of cheering echoes into the room from somewhere far beyond in the darkness.', 'You win! You absorb some of the Evil Wizard\'s ill-gotten wealth.', 'Victory is yours! The Evil Wizard grinds his teeth with rage as you boop him on the snoot.']
defeat_messages = ['You lose. The Evil Wizard sticks his tongue up your nose.', 'You lose. The Evil Wizard shrinks your head.', 'You lose. The Evil Wizard laughs and calls you names in an eldritch tongue long forgotten by mortal man.', 'You lose. You hear shrieks of agony from the outer darkness and fear grips your heart.', 'The Wizard comes out on top this time. A thick, foul smell oozes from him, threatening your consciousness.', 'The Wizard waves his hand and adds your money to his untold hoard of riches. You lose.', 'You lose. You get nothing. Good day.', 'Your best wasn\'t good enough. You lose. The Wizard hocks a loogie of a color unknown to this world onto your shoe.', 'You lose. You can feel your bones beginning to soften under the Wizard\'s evil stare.']
tie_messages = ['You reach a stalemate with the Evil Wizard. The fates sneeze in your mouth.', "It's a tie. So close, yet so far away.", "It's a tie. The Wizard's hand oozes from his robe to take your money."]
player_bust_messages = ["Bust! The Evil Wizard will have your eyes for this!", "Bust! Your greed has driven you to destruction.", "Bust! Has the Wizard bent your mind to his own purposes?", "Bust! The room swims before your eyes as the Evil Wizard's miasma enfolds you.", "Bust! Who needs enemies when you can defeat yourself?", "Bust! You feel a hand close around your throat. It is your own! The Wizard cackles with delight.", "You Bust!"]
dealer_bust_messages = ["The Evil Wizard busts! His powers must be fading...", "The Evil Wizard busts! He stares impotently at his wizened hands.", "The Evil Wizard busts! He stomps his feet like a petulant child.", "The Evil Wizard busts! For a moment, you can see his skeleton flash through his ancient flesh.", "The Evil Wizard busts! You hear a soft clink as his money materializes in your coin purse.", "The Evil Wizard busts! The foul creature howls with rage, his eyes seething liquid flame."]

def message(message_array):
    """
    Prints a random message from the array of messages passed as an argument.
    """
    print(message_array[random.randrange(0, len(message_array))])

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
        answer = input("Do you dare brave the Evil Wizard's wrath again? [y/n]")
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


def goodbye(bank):
    if bank == 1000:
        print("Thank you for playing. You leave the Evil Wizards's dungeon with the same money you brought into it, your head and dignity intact.")
    elif bank - 1000 > 0:
        print(
            f"Thank you for playing. You leave the Evil Wizard's dungeon ${bank - 1000} richer. Well done. Well done indeed. Go forth and prosper.")
    else:
        print(
            f"You leave the Evil Wizard's dungeon ${abs(bank - 1000)} poorer. You poor sap. Get out of my sight.")


print("$" * 40)
print("Welcome to Evil Wizard's Blackjack!\nPrepare yourself, weakling!")
print("$" * 40)
bank = 1000
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

    if bank == 0:
        print("You have lost everything. You leave in shame, fortunate even to retain your life. Goodbye.")
        break

    print(f"Your bank: ${bank}")
    bet = input('Place your bet: ')
    if '$' in bet:
        bet = bet.replace('$', '')
    if '.' in bet:
        bet = bet.split('.')
        try:
            cents = int(bet[1])
            if cents != 0:
                print("Your bet must be a whole number.")
                continue
            bet = bet[0]
        except ValueError:
            print("Your bet must be a number.")
            continue
    try:
        bet = int(bet)
    except ValueError:
        print("Your bet must be a number.")
        continue
    if bet < 1:
        print('Your bet must be a positive number.')
        continue
    if bet > bank:
        print(f"You don't have ${bet} to bet.")
        continue

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
        print(f"Evil Wizard's hand: [X] {dealer_hand[1]['name']}")
        player_total = add_cards(player_hand)
        if len(player_hand) == 2 and player_total == 21:
            print("BLACKJACK!!!")
            time.sleep(1)
            print("Can this be the end for the Evil Wizard?...")
            time.sleep(1)
            print("Evil Wizard's hand:", end=" ")
            for card in dealer_hand:
                print(card["name"], end=" ")
            print()
            dealer_total = add_cards(dealer_hand)
            time.sleep(1)
            if player_total > dealer_total:
                bank += bet
                message(victory_messages)
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
        bank += bet
        message(victory_messages)
        if play_again():
            continue
        else:
            break
    elif player_bust:
        bank -= bet
        message(player_bust_messages)
        if play_again():
            continue
        else:
            break
    else:
        # dealer's turn
        print("#" * 40)
        print("Evil Wizard's turn!")
        print("#" * 40)
        while True:
            print("*" * 40)
            print('Your hand:', end=" ")
            for card in player_hand:
                print(card["name"], end=" ")
            print()
            print("Evil Wizard's hand:", end=" ")
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
                print('The Evil Wizard hits.')
                time.sleep(1)
                deal_card(dealer_hand, deck)
            elif dealer_total >= player_total:
                break

        if dealer_bust:
            bank += bet
            message(dealer_bust_messages)
            if play_again():
                continue
            else:
                goodbye(bank)
                break
        elif dealer_charlie:
            bank -= bet
            message(defeat_messages)
            if play_again():
                continue
            else:
                break
        elif dealer_total == player_total:
            bank -= bet
            message(tie_messages)
            if play_again():
                continue
            else:
                goodbye(bank)
                break
        elif dealer_total > player_total:
            bank -= bet
            message(defeat_messages)
            if play_again():
                continue
            else:
                goodbye(bank)
                break
        else:
            bank += bet
            message(victory_messages)
            if play_again():
                continue
            else:
                goodbye(bank)
                break
    break
