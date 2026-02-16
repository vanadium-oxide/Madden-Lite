class AmericanFootballTeam:
    def __init__(self, team_name, home_city, coaching_staff=None, roster=None):
        self.team_name = team_name
        self.home_city = home_city
        self.coaching_staff = coaching_staff if coaching_staff is not None else []
        self.roster = roster if roster is not None else []
    
    def add_player(self, player):
        self.roster.append(player)
    
    def add_coach(self, coach):
        self.coaching_staff.append(coach)
    
    def __repr__(self):
        return f"AmericanFootballTeam(name='{self.team_name}', city='{self.home_city}')"