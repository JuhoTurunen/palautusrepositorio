class Player:
    def __init__(self, data):
        self.name = data.get("name")
        self.team = data.get("team")
        self.goals = data.get("goals")
        self.assists = data.get("assists")

    def __str__(self):
        a = (f"{self.name}{" " * max(28-len(self.name), 1)}{self.team}   " 
        f"{self.goals}{" " * max(3-len(str(self.goals)), 1)}+ "
        f"{self.assists}{" " * max(3-len(str(self.assists)), 1)}= "
        f"{self.goals + self.assists}")
        return a