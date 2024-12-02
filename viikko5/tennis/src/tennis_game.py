class TennisGame:
    DEUCE_THRESHOLD = 3
    WIN_THRESHOLD = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.tied_to_game_state_str()

        if self.player1_score < self.WIN_THRESHOLD and self.player2_score < self.WIN_THRESHOLD:
            score1 = self.number_to_tennis_score(self.player1_score)
            score2 = self.number_to_tennis_score(self.player2_score)
            return f"{score1}-{score2}"

        return self.lead_to_game_state_str()

    def tied_to_game_state_str(self):
        if self.player1_score >= self.DEUCE_THRESHOLD:
            return "Deuce"
        tennis_score = self.number_to_tennis_score(self.player1_score)
        return f"{tennis_score}-All"

    def lead_to_game_state_str(self):
        game_balance = self.player1_score - self.player2_score
        leading_player = self.player1_name if game_balance > 0 else self.player2_name
        lead = abs(game_balance)
        if lead == 1:
            return f"Advantage {leading_player}"
        return f"Win for {leading_player}"

    def number_to_tennis_score(self, number):
        match number:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case 3:
                return "Forty"
