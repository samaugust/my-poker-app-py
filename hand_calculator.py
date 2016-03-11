import random
import itertools

def deck():
  
  ranks = ["2","3","4","5","6","7","8","9","10","11","12","13","14"]
  suits = ["a","b","c","d"]
  composite = []
  
  for rank in ranks:
    for suit in suits:
      composite.append(rank + suit)
  
  random.shuffle(composite)
  
  return composite

def r(cards):
  
  rank_list = []
  
  for card in cards:
    rank_list.append(int(card[0:-1]))
  
  rank_list.sort()
  
  return rank_list

def s(cards):
  
  suit_list = []
  
  for card in cards:
    suit_list.append(card[-1])
  
  return suit_list
  
def which_rank_occurs_n_times(rank_list, n):
  
  desired_rank = []
  rank_dic = {}
  
  for rank in rank_list:
    if rank in rank_dic:
      rank_dic[rank] += 1
    else:
      rank_dic[rank] = 1
      
  for rank in rank_dic:
    if rank_dic[rank] == n:
      desired_rank.append(rank)
      
  return desired_rank[0] if len(desired_rank) == 1 else desired_rank

def isolate_kickers(rank_list, n):
  
  kickers = []
  
  for rank in rank_list:
    if rank != which_rank_occurs_n_times(rank_list, n):
      kickers.append(rank)
  
  return kickers

def assess_kickers(hands, i, n):
  
  best_hand = []
  kicker = 0
  
  for hand_unrefined in hands:
    nonpair_cards = isolate_kickers(r(hand_unrefined), n)
    
    if nonpair_cards[i] > kicker:
      kicker = nonpair_cards[i]
      best_hand = [hand_unrefined]
    elif nonpair_cards[i] == kicker:
      best_hand.append(hand_unrefined)
      
  if len(best_hand) == 1 or i == 0:
    return best_hand
  
  i -= 1
  return assess_kickers(hands, i, n)

def uniques(seq): 
   # order preserving
   uniques = []
   [uniques.append(i) for i in seq if not uniques.count(i)]
   return uniques
    
def all_hands_from_cards(cards):
  
  all_hands = []
  
  if len(cards) == 7:
    while (len(all_hands) < 21):
      random.shuffle(cards)
      random_hand = cards[0:5]
      random_hand.sort()
      all_hands.append(random_hand)
      all_hands = uniques(all_hands)
  elif len(cards) == 6:
    while (len(all_hands) < 6):    
      random.shuffle(cards)
      random_hand = cards[0:5]
      random_hand.sort()
      all_hands.append(random_hand)
      all_hands = uniques(all_hands)
  else:
    return [cards]
  
  return all_hands



def straight_flush(cards):
  suit = s(cards)
  rank = r(cards)
  
  if suit[0] == suit[1] and suit[1] == suit[2] and suit[2] == suit[3] and suit[3] == suit[4]:
    if rank[4] - rank[3] == 1 and rank[3] - rank[2] == 1 and rank[2] - rank[1] == 1 and rank[1] - rank[0] == 1 and  rank[3] == 13:
      return "royal flush"
    elif rank[4] - rank[3] == 1 and rank[3] - rank[2] == 1 and rank[2] - rank[1] == 1 and rank[1] - rank[0] == 1:
      return True
    elif rank[3] - rank[2] == 1 and rank[2] - rank[1] == 1 and rank[1] - rank[0] == 1 and rank[4] - rank[0] == 12 and rank[4] == 14:
      return True
    else:
      return False
  else:
    return False

def quads(cards):
    
  rank = r(cards)
  
  if (rank[0] == rank[1] and rank[1] == rank[2] and rank[2] == rank[3]) or (rank[1] == rank[2] and rank[2] == rank[3] and rank[3] == rank[4]):
    return True
  else:
    return False

def full_house(cards):
    
  rank = r(cards)

  if ((rank[0] == rank[1] and rank[1] == rank[2]) and rank[3] == rank[4]) or (rank[0] == rank[1] and (rank[2] == rank[3] and rank[3] == rank[4])):
    return True
  else:
    return False

def flush(cards):
    
  suit = s(cards)
  
  if suit[0] == suit[1] and suit[1] == suit[2] and suit[2] == suit[3] and suit[3] == suit[4]:
    return True
  else:
    return False


def straight(cards):

  rank = r(cards)
  
  if rank[4] - rank[3] == 1 and rank[3] - rank[2] == 1 and rank[2] - rank[1] == 1 and rank[1] - rank[0] == 1:
    return True
  elif rank[3] - rank[2] == 1 and rank[2] - rank[1] == 1 and rank[1] - rank[0] == 1 and rank[4] - rank[0] == 12 and rank[4] == 14:
    return True
  else:
    return False

def trips(cards):
    
  rank = r(cards)
  
  if (rank[0] == rank[1] and rank[1] == rank[2]) or (rank[1] == rank[2] and rank[2] == rank[3]) or (rank[2] == rank[3] and rank[3] == rank[4]):
    return True
  else:
    return False

def two_pair(cards):
    
  rank = r(cards)
  
  if (rank[0] == rank[1] and rank[2] == rank[3]) or (rank[1] == rank[2] and rank[3] == rank[4]) or (rank[0] == rank[1] and rank[3] == rank[4]):
    return True
  else:
    return False

def pair(cards):
    
  rank = r(cards)
  
  if rank[0] == rank[1] or rank[1] == rank[2] or rank[2] == rank[3] or rank[3] == rank[4]:
    return True
  else: 
    return False



def best_quads(hands):

  best_hand = []
  highest_rank = 0

  for hand_unrefined in hands:
    hand = r(hand_unrefined)

    if which_rank_occurs_n_times(hand, 4) > highest_rank:
      best_hand = [hand_unrefined]
      highest_rank = which_rank_occurs_n_times(hand, 4)
    
    elif which_rank_occurs_n_times(hand, 4) == highest_rank:
      best_hand.append(hand_unrefined)

  if len(best_hand) == 1:
    return best_hand
  
  return assess_kickers(best_hand, 4, 0)

def best_full_house(hands):

  best_hand = []
  highest_rank = 0

  for hand_unrefined in hands:
    hand = r(hand_unrefined)
    
    if which_rank_occurs_n_times(hand, 3) > highest_rank:
      best_hand = [hand_unrefined]
      highest_rank = which_rank_occurs_n_times(hand, 3)
    
    elif which_rank_occurs_n_times(hand, 3) == highest_rank:
      best_hand.append(hand_unrefined)

  if len(best_hand) > 1:

    highest_rank = 0

    for hand_unrefined in best_hand:
      hand = r(hand_unrefined)

      if which_rank_occurs_n_times(hand, 2) > highest_rank:
        best_hand = [hand_unrefined]
        highest_rank = which_rank_occurs_n_times(hand, 2)
      
      elif which_rank_occurs_n_times(hand, 2) == highest_rank:
        best_hand.append(hand_unrefined)
    return best_hand
  else: 
    return best_hand

def best_flush(hands):
  return assess_kickers(hands, 4, 1)

def best_straight(hands):
    
  highest_rank_sum = 0
  best_hand = []
  
  for hand in hands:

    ## Reassign the rank value of the ace when it is part of the low straight. 
    rank = r(hand)
    if rank == [2,3,4,5,14]:
      rank[4] = 1

    rank_sum = sum(rank)

    if rank_sum > highest_rank_sum:
      highest_rank_sum = rank_sum
      best_hand = [hand]

    elif rank_sum == highest_rank_sum:
      best_hand.append(hand)
  return best_hand

def best_trips(hands):

  best_hand = []
  highest_rank = 0
  
  for hand_unrefined in hands:
    hand = r(hand_unrefined)
    
    if which_rank_occurs_n_times(hand, 3) > highest_rank:
      best_hand = [hand_unrefined]
      highest_rank = which_rank_occurs_n_times(hand, 3)
    
    elif which_rank_occurs_n_times(hand, 3) == highest_rank:
      best_hand.append(hand_unrefined)

  if best_hand.length == 1:
    return best_hand
  
  return assess_kickers(best_hand, 1, 3)

def best_two_pair(hands):
    
  best_hand = []
  top_pair_max = 0
  bottom_pair_max = 0
  kicker_max = 0
  
  for hand_unrefined in hands:
    hand = r(hand_unrefined)
    top_pair = max((which_rank_occurs_n_times(hand, 2)))
    
    if top_pair > top_pair_max:
      top_pair_max = top_pair
      best_hand = [hand_unrefined]
    
    elif top_pair == top_pair_max:
      best_hand.append(hand_unrefined)
          
  if len(best_hand) > 1:
    
    for hand_unrefined in best_hand:
      hand = r(hand_unrefined)
      bottom_pair = min((which_rank_occurs_n_times(hand, 2)))
  
      if bottom_pair > bottom_pair_max:
        bottom_pair_max = bottom_pair
        best_hand = [hand_unrefined]
      
      elif bottom_pair == bottom_pair_max:
        best_hand.append(hand_unrefined)
  
    if len(best_hand) > 1:
        
      for hand_unrefined in best_hand:
        hand = r(hand_unrefined)
        kicker = which_rank_occurs_n_times(hand, 1)
        if kicker > kicker_max:
          kicker_max = kicker
          best_hand = [hand_unrefined]
    
        elif kicker == kicker_max:
          best_hand.append(hand_unrefined)
      return best_hand
    else:
      return best_hand
  else:
    return best_hand

def best_pair(hands):
  
  best_hand = []
  top_pair = 0
  
  for hand_unrefined in hands:
    hand = r(hand_unrefined)
    
    if which_rank_occurs_n_times(hand, 2) > top_pair:
      top_pair = which_rank_occurs_n_times(hand, 2)
      best_hand = [hand_unrefined]
    
    elif which_rank_occurs_n_times(hand, 2) == top_pair:
      best_hand.append(hand_unrefined)
  
  if len(best_hand) == 1:
    return best_hand 
   
  return assess_kickers(best_hand, 2, 2)

def best_air(hands):
    return assess_kickers(hands, 4, 1)



def evaluate_hand(cards):
  if straight_flush(cards) == "royal flush":
    return 10 
  if straight_flush(cards):
    return 9 
  if quads(cards):
    return 8 
  if full_house(cards):
    return 7 
  if flush(cards):
    return 6 
  if straight(cards):
    return 5
  if trips(cards):
    return 4 
  if two_pair(cards):
    return 3
  if pair(cards):
    return 2 
  return 1

def best_hand(hands):

  best_hand = []
  best_hand_score = 0

  for hand in hands:
    if evaluate_hand(hand) > best_hand_score:
      best_hand = [hand]
      best_hand_score = evaluate_hand(hand)
    elif evaluate_hand(hand) == best_hand_score:
      best_hand.append(hand)

  if len(best_hand) > 1:
    if best_hand_score == 1:
      return best_air(best_hand)
    elif best_hand_score == 2:
      return best_pair(best_hand)
    elif best_hand_score == 3:
      return best_two_pair(best_hand)
    elif best_hand_score == 4:
      return best_trips(best_hand)
    elif best_hand_score == 5 or best_hand_score == 9:
      return best_straight(best_hand)
    elif best_hand_score == 6:
      return best_flush(best_hand)
    elif best_hand_score == 7:
      return best_full_house(best_hand)
    elif best_hand_score == 8:
      return best_quads(best_hand)
    else:
      return best_hand
  else:
    return best_hand

def winning_hand(hand):

  if len(hand) == 1:
    hand = list(itertools.chain(*hand))
  else:
    hand = hand[0]

  if straight_flush(hand) == "royal flush":
    return "ROYAL FLUSH!" 
  if straight_flush(hand):
    return "STRAIGHT FLUSH!" 
  if quads(hand):
    return "FOUR OF A KIND!" 
  if full_house(hand):
    return "FULL HOUSE!" 
  if flush(hand):
    return "FLUSH!" 
  if straight(hand):
    return "STRAIGHT!" 
  if trips(hand):
    return "THREE OF A KIND!" 
  if two_pair(hand):
    return "TWO PAIR!" 
  if pair(hand):
    return "PAIR!" 
  return "COMPLETE AIR"