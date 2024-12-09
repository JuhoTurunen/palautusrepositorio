from statistics import Statistics  # type: ignore
from player_reader import PlayerReader
from matchers import And, Not, Or, All, HasAtLeast, HasFewerThan, PlaysIn


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(HasAtLeast(5, "goals"), HasAtLeast(20, "assists"), PlaysIn("PHI"))

    for player in stats.matches(matcher):
        print(player)

    matcher = And(HasFewerThan(2, "goals"), Not(HasFewerThan(20, "assists")))

    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    matcher = Or(HasAtLeast(45, "goals"), HasAtLeast(70, "assists"))
    for player in stats.matches(matcher):
        print(player)
    print()
    matcher = And(HasAtLeast(70, "points"), Or(PlaysIn("NYR"), PlaysIn("FLA"), PlaysIn("BOS")))
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
