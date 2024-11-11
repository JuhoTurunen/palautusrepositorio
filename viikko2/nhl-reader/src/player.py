class Player:
    def __init__(self, data):
        self.name = data.get("name")
        self.team = data.get("team")
        self.goals = data.get("goals")
        self.assists = data.get("assists")

    def __str__(self):
        return f"{self.name} team {self.team}  goals {self.goals} assists {self.assists}"