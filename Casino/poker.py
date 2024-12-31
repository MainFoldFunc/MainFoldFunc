import random

SUITS = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    deck = [f'{rank} - {suit}' for suit in SUITS for rank in RANKS]
    return deck


def get_card_info(card):
    rank, suit = card.split(' - ')
    return rank, suit


def evaluate_hand(hand):
    ranks = [get_card_info(card)[0] for card in hand]
    suits = [get_card_info(card)[1] for card in hand]
    rank_counts = {rank: ranks.count(rank) for rank in ranks}
    is_flush = len(set(suits)) == 1
    sorted_ranks = sorted([RANKS.index(rank) for rank in ranks], reverse=True)

    is_straight = False
    if len(set(sorted_ranks)) == 5 and (max(sorted_ranks) - min(sorted_ranks) == 4):
        is_straight = True

    if is_flush and is_straight:
        if sorted_ranks == [8, 9, 10, 11, 12]:
            return (10, sorted_ranks) 
        return (9, sorted_ranks) 
    if 4 in rank_counts.values():
        return (8, sorted_ranks)
    if 3 in rank_counts.values() and 2 in rank_counts.values():
        return (7, sorted_ranks) 
    if is_flush:
        return (6, sorted_ranks) 
    if is_straight:
        return (5, sorted_ranks) 
    if 3 in rank_counts.values():
        return (4, sorted_ranks) 
    if list(rank_counts.values()).count(2) == 2:
        return (3, sorted_ranks) 
    if 2 in rank_counts.values():
        return (2, sorted_ranks)
    return (1, sorted_ranks)

def winner(player_deck, ai_1_deck, ai_2_deck, ai_3_deck, ai_4_deck):
    hands = {
        'Player': player_deck,
        'AI 1': ai_1_deck,
        'AI 2': ai_2_deck,
        'AI 3': ai_3_deck,
        'AI 4': ai_4_deck
    }

    evaluated_hands = {}
    for player, hand in hands.items():
        hand_value = evaluate_hand(hand)
        evaluated_hands[player] = hand_value

    sorted_players = sorted(evaluated_hands.items(), key=lambda x: x[1], reverse=True)

    winner = sorted_players[0][0]
    return winner

def poker(full_money):

    ask_m = True
    while ask_m:
        money = int(input(f"How much money would you like to deposit? You have {full_money} left: "))
        if money < 0 or money > full_money:
            print("Invalid amount of money, please enter again.")
        else:
            ask_m = False

    print("You are playing with 4 AI opponents.")

    deck = create_deck()
    random.shuffle(deck)

    player_deck = [deck.pop() for _ in range(5)]
    ai_1_deck = [deck.pop() for _ in range(5)]
    ai_2_deck = [deck.pop() for _ in range(5)]
    ai_3_deck = [deck.pop() for _ in range(5)]
    ai_4_deck = [deck.pop() for _ in range(5)]

    print("Your cards:", player_deck)
    print(f"AI 1's cards: {ai_1_deck}")
    print(f"AI 2's cards: {ai_2_deck}")
    print(f"AI 3's cards: {ai_3_deck}")
    print(f"AI 4's cards: {ai_4_deck}")

    winner_player = winner(player_deck, ai_1_deck, ai_2_deck, ai_3_deck, ai_4_deck)
    print(f"{winner_player} wins!")
    if winner_player != player_deck:
        money -= money
    else:
        money*money
    return money
