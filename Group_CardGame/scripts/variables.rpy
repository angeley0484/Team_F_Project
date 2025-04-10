default player_name = "Player 1"
default player2_name = "Player 2"
default player_id = 0

default game_server = "0.0.0.0"  # Placeholder for game server IP address
default opponent_id = 0

# Placeholder for IP, will be set later if get_ip() is available
default ip = "Unknown"

init -98 python:
    import random
    # Make sure the classes are loaded (they are, from classes.rpy init -99)
    # from store import playerdata, MultiplayerOpponent # Not strictly needed due to init order

    # --- Placeholder for get_ip ---
    # If get_ip is your custom function, define or import it here.
    # Otherwise, this will cause a NameError.
    # Example using socket (standard library):
    def get_ip():
        try:
            import socket
            # Get local hostname
            hostname = socket.gethostname()
            # Get IP address corresponding to the hostname
            ip_address = socket.gethostbyname(hostname)
            # Filter out loopback addresses if necessary
            if ip_address.startswith("127."):
                pass
            return ip_address
        except Exception as e:
            print(f"Could not determine IP address: {e}")
            return "127.0.0.1" # Fallback IP
    # --- End Placeholder ---


    # Update store variables using the store prefix
    store.player_id = random.randint(1, 10000000000)

    # Access default variables using store. prefix when creating objects
    # Ensure playerdata class is defined (it is in classes.rpy init -99)
    store.player = playerdata(store.player_name, store.player_id)

    # Call get_ip and store the result in the store variable 'ip'
    store.ip = get_ip()

    # Ensure MultiplayerOpponent class is defined (it is in classes.rpy init -99)
    # Access default variables using store. prefix
    store.player2 = MultiplayerOpponent(store.player2_name, store.opponent_id, server=store.game_server)
