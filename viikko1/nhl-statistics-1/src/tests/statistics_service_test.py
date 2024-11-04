import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.players = StatisticsService(PlayerReaderStub())

    def test_search(self):
        search_result = self.players.search("Lemieux")
        self.assertEqual(search_result.name, "Lemieux")
        self.assertEqual(search_result.team, "PIT")
        self.assertEqual(search_result.goals, 45)
        self.assertEqual(search_result.assists, 54)

    def test_search_fail(self):
        search_result = self.players.search("fail")
        self.assertEqual(search_result, None)

    def test_team(self):
        team_players = self.players.team("EDM")
        self.assertEqual(team_players[0].name, "Semenko")
        self.assertEqual(team_players[0].team, "EDM")
        self.assertEqual(team_players[0].goals, 4)
        self.assertEqual(team_players[0].assists, 12)
        self.assertEqual(team_players[1].name, "Gretzky")
        self.assertEqual(team_players[1].team, "EDM")
        self.assertEqual(team_players[1].goals, 35)
        self.assertEqual(team_players[1].assists, 89)

    def test_top(self):
        top_players = self.players.top(2)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[0].team, "EDM")
        self.assertEqual(top_players[0].goals, 35)
        self.assertEqual(top_players[0].assists, 89)
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[1].team, "PIT")
        self.assertEqual(top_players[1].goals, 45)
        self.assertEqual(top_players[1].assists, 54)
