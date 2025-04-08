label start:
    $ player_name = "Player1"  # You can dynamically ask for this input from the player

    # Join the game via the server
    $ join_message = join_game(player_name)
    "Server Response: [join_message]"

    # Let's assume we update player stats here after a round
    $ update_message = update_player_stats(player_name, 5, 2, 100)  # Example stats
    "Server Response: [update_message]"

    # Get the game state (to display player scores, wins, etc.)
    $ players = get_game_state()
    "Current Game State:"
    for player in players:
        "Player [player['name']] - Wins: [player['wins']], Losses: [player['losses']], Score: [player['score']]"
