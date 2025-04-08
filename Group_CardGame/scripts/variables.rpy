
default player_name = "Player 1"
default player2_name = "Player 2"

default player_id = rand.int(1, 10000000000)

default player = Player(player_name, player_id)

default ip = get_ip()
default game_server = [0.0.0.0] ### Placeholder for game server IP address ###  

default player2_name = "Player 2"
default opponent_id = 0


### updates from server when connected
default player2 = MultiplayerPlayer(player2_name, opponent_id)


