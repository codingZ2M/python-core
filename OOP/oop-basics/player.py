class Player:

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
# pos = position

    def get_play_pos(self):
        return self.pos

    def get_play_name(self):
        return self.name

# 1 = PG(Point Guard) 2 = SG(Shooting Guard) 3 = SF(Short Forward) 4 = PF(Power Forward) 5 = C(Center)
collins = Player("Collins", 8)
bogdan = Player("Bogdan", 2)
trae = Player("Trae", 7)
capela = Player("Capela", 5)

players = [collins, bogdan, trae, capela] # List

def get_player(players_list):
    positions = []
    for object in players_list:
        position = object.get_play_pos()
        positions.append( position)

        for index, position in enumerate(positions, 0):
           if position < max(positions):
              if position == min(positions):
                 player_object = players_list[index]
                 player_name = player_object.get_play_name()
                 break


    print(f"Player Position Is: {position} & Player Name Is: {player_name}")


get_player(players)