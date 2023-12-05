from itertools import combinations
from collections import deque
from copy import deepcopy

def select_card(rod, own_cards, n):
    own_card = deepcopy(own_cards)
    select_card = list(combinations(own_cards, 2))
    for card in select_card:
        if sum(card) == n+1:
            print("???",card)
            own_card.remove(card[0])
            own_card.remove(card[1])

            return rod, own_card, True

    return rod, own_card, False

def solution(coin, cards):
    n = len(cards)
    user_cards = cards[:n//3]
    cards = cards[n//3:]

    max_rod = 1
    game_rod = 1
    
    que = deque([[user_cards, cards, game_rod, coin]])

    while len(que) != 0: 
        print("que: ",que)
        own_cards, deck, rod, own_coin = que.popleft()
        #print("own_cards, deck, rod, own_coin: ",own_cards, deck, rod, own_coin)
        #카드가 1장 이하라면 종료
        if len(deck) <= 1 or own_coin <= 1:
            max_rod = max(max_rod,rod)
            break
        
        #카드 뽑기
        draw_card = deck[:2]
        deck = deck[2:]

        use_coin = 0 if own_coin == 0 else (1 if own_coin == 1 else 2)
        use_range = [[0,0,0],[0,2,2]]

        for c1,c2,c3 in use_range:
            own_cards = own_cards + draw_card[c1:c2]
            print("own_card", own_cards)
            r, o, f = select_card(rod, own_cards, n)
            print("rod, own_card, flag: ",r,o,f)
            if f == False:
                max_rod = max(max_rod, r)
                print("라운드 갱신: ",max_rod)

            else:
                if len(deck) <= 1:
                    max_rod = max(max_rod, r+1)
                    continue

                if own_coin - c3 <= 0:
                    que.append([o, deck, r+1, 0])
                else:
                    print("c3",c3)
                    que.append([o, deck, r+1, own_coin - c3])

    return max_rod


print(solution(2, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]))