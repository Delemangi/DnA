class Ranking:
    def calculate(self, N, z):
        main_team = tuple(z[:3])
        main_score = self.score(main_team)
        teams = []
        players = z[3:]
        players.sort()

        while len(players):
            team = []

            team.append(players.pop(0))
            team.append(players.pop(-1))

            for p in reversed(players):
                if self.score(team + [p]) > main_score:
                    players.remove(p)
                    team.append(p)
                    teams.append(team)

                    break
            else:
                break

        return len(teams) + 1

    def score(self, team):
        return team[0] + team[1] + team[2] - min(team)
