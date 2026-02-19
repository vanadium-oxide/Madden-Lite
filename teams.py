class FootBallTeam:
    def __init__(self, team_name, division, conference, city, team_roster=None, team_logo=None):
        self.team_name = team_name
        self.division = division
        self.conference = conference
        self.city = city
        self.team_roster = team_roster if team_roster is not None else []
        self.team_logo = team_logo


    def add_player(self, player):
        self.roster.append(player)
    
    def add_coach(self, coach):
        self.coaching_staff.append(coach)
    
    def __repr__(self):
        return f"FootballTeam(name='{self.team_name}', city='{self.city}')"