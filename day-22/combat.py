from collections import namedtuple

Turn = namedtuple("Turn", ["deck", "card"])

class Combat:
    def __init__(self,player_1,player_2):
        self.player_1 = player_1
        self.player_2 = player_2

        self.cache = {
            0 : 
            (
            Turn(deck=player_1, card=None),
            Turn(deck=player_2, card=None)
            )
        }

    @staticmethod
    def _get_next(current):
        if any(turn.deck==[] for turn in current):
            raise IndexError("No next.")
        
        current = [
            Turn(deck=player.deck[1:], card=player.deck[0])
            for player in current
        ]

        cards = sorted((turn.card for turn in current),reverse=True)

        winner = max(range(2), key=lambda i: current[i].card)

        current[winner].deck.extend(cards)

        return [
            Turn(deck=current[i].deck, card=current[i].card)
            for i in range(2)
        ]

    def __getitem__(self,index):
        try:
            last_cache_key = sorted(self.cache.keys())[-1]

            while index not in self.cache:
                next = self._get_next(self.cache[last_cache_key])
                self.cache[last_cache_key+1] = next
                last_cache_key += 1

            p_1, p_2 = self.cache[index]
            return type(self)(p_1.deck, p_2.deck)
        
        except IndexError:
            raise IndexError("Game already ended.") from None

    def __repr__(self):
        return f"""Player 1 - {len(self.player_1)} cards: {self.player_1}
        \r\rPlayer 2 - {len(self.player_2)} cards: {self.player_2}"""

    def play(self):
        for turn in self:
            pass

        return turn

    @property
    def winner(self):
        if self.player_1 and self.player_2:
            raise ValueError("Game hasn't ended yet.")

        return 1 if self.player_1==[] else 0

    @property
    def score(self):
        if self.player_1 and self.player_2:
            raise ValueError("Game hasn't ended yet.")
        
        score = 0
        for card_lst in (self.player_1, self.player_2):
            for i, card in enumerate(card_lst[::-1]):
                score += card * (i+1)

        return score

    @classmethod
    def parse_from_file(cls,fh):
        player_1_raw, player_2_raw = fh.read().split("\n\n")

        player_1 = [int(card.strip()) for card in player_1_raw.split("\n")[1:]]
        player_2 = [int(card.strip()) for card in player_2_raw.split("\n")[1:]]

        return cls(player_1,player_2)

class RecursiveCombat(Combat):
    def __init__(self,player_1,player_2):
        super().__init__(player_1,player_2)
        self.already_seen = { 
            (tuple(self.cache[0][0].deck), tuple(self.cache[0][1].deck)) 
        }

    def _get_next(self,current):
        if any(player.deck==[] for player in current):
                raise IndexError("No next.")

        current = [
            Turn(deck=player.deck[1:], card=player.deck[0])
            for player in current
        ]

        decks_tuple = (tuple(current[0].deck), tuple(current[1].deck))
        # if the same sequence was already played, player 1 wins
        if decks_tuple in self.already_seen:
            current[1] = Turn(deck=[], card=current[1].card)
        else:
            self.already_seen.add(decks_tuple)

            # if for both players value of card <= number of cards in hand, winner is determined by another game
            if all(player.card<=len(player.deck) for player in current):
                winner = RecursiveCombat(
                    *(current[i].deck[:current[i].card] for i in range(2))
                ).play().winner
            else:
                winner = max(range(2), key=lambda i: current[i].card)

            loser = not winner
            cards = [current[winner].card, current[loser].card]

            current[winner].deck.extend(cards)

        return [
            Turn(deck=current[i].deck, card=current[i].card)
            for i in range(2)
        ]
