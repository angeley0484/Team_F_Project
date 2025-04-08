init python:
    import requests

    def get_ip():
        try:
            # Fetch the public IP address using an external service
            response = requests.get("https://api.ipify.org?format=text")
            if response.status_code == 200:
                return response.text
            else:
                return ip =  response.text
        except:
            return "Unknown IP Failed to fetch IP address"

    ### Placeholder for pinging game server for connection availability
    def ping_server(ip):
        try:
            response = requests.get(f"http://{ip}/ping")
            if response.status_code == 200:
                return response.json().get("status") == "ok"
            else:
                return excecpt("Server not reachable")
                

        except:
            return False
    
    ### Send Player data to the server
    def send_player_data(ip, player_id, player_name):
        try:
            data = {
                "player_id": player_id,
                "player_name": player_name

            }
            response = requests.post(f"http://{ip}/register", json=data)
            return response.status_code == 200
        except:
            return False

    def receive_opponent_data(ip):
        """
        Fetch the opponent player's data (player_id and player_name) from the server.
        """
        try:
            response = requests.get(f"http://{ip}/opponent")
            if response.status_code == 200:
                data = response.json()
                opponent_id = data.get("player_id")
                opponent_name = data.get("player_name")
                return opponent_id, opponent_name
            else:
                return None, None
        except:
            return None, None