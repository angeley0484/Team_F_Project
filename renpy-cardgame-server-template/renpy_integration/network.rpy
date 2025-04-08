# renpy_integration/network.rpy

init python:
    import requests

    # Join the game
    def join_game(player_name):
        url = "http://127.0.0.1:5000/join"
        response = requests.post(url, json={"name": player_name})
        if response.status_code == 200:
            renpy.pause(1, hard=True)  # Wait for the server to respond
            return response.json()['message']
        else:
            return "Failed to join game"

    # Update player's stats in the game
    def update_player_stats(player_name, wins, losses, score):
        url = "http://127.0.0.1:5000/update_player"
        data = {
            "name": player_name,
            "wins": wins,
            "losses": losses,
            "score": score
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            renpy.pause(1, hard=True)  # Wait for the server to respond
            return response.json()['message']
        else:
            return "Failed to update stats"

    # Get game state
    def get_game_state():
        url = "http://127.0.0.1:5000/game_state"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['players']
        else:
            return []
