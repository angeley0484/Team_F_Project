init -99 python:
    ### TRIPLE TRIAD BASE GAME CLASSES ###
    ### This file contains the classes for the Triple Triad game. ###
    ### The classes include Card, Deck, Player, and MultiplayerPlayer. ###
    ### Each class has methods for handling game logic and player actions. ###

    #Use to create cards from images and assign side values to them
    import random 

    class Card:
        def __init__(self, north, south, east, west, image_path):
            # Initialize the card's directional values
            self.north = north
            self.south = south
            self.east = east
            self.west = west
            
            # Store the image path and create an image displayable
            self.image_path = image_path
            self.image = Image(image_path)
        
        def get_value(self, direction):
            """Get the value for a specific direction"""
            if direction == "north":
                return self.north
            elif direction == "south":
                return self.south
            elif direction == "east":
                return self.east
            elif direction == "west":
                return self.west
            return None
        
        def display(self):
            """Return the card's image displayable"""
            return self.image
    
    class playerdata:
        def __init__(self, name, id):
            # Initialize the player's name and ID
            self.name = name
            self.id = id
            self.hand = []  # Player's hand of cards

    class Deck:
        def __init__(self):
            # Initialize an empty list of cards with a maximum of 10 cards
            self.cards = []
            self.max_cards = 10
            if len(self.cards) > self.max_cards:
                raise ValueError("Deck cannot contain more than 10 cards")
        
        def add_card(self, card):
            """Add a card to the deck"""
            if len(self.cards) < self.max_cards:
                self.cards.append(card)
            else:
                print("Deck is full! Cannot add more cards.")
        
        def shuffle(self):
            """Shuffle the deck of cards"""
            random.shuffle(self.cards)
        
        def draw_card(self):
            """Draw a card from the top of the deck"""
            if self.cards:
                return self.cards.pop(0)
            return None

    class Hand:
        def __init__(self, deck):
            # Initialize an empty hand of cards
            self.cards = []
            self.max_cards = 5
            while len(self.cards) < self.max_cards:
                card = deck.draw_card()
                if card:
                    self.cards.append(card)            

    class Player:
        def __init__(self, name, id):
            # Initialize the player's name and an empty hand of cards
            self.name = name
            self.id = id
            self.deck = chosenDeck
            self.hand = []

        def draw(self, deck):
            """Draw a card from the deck and add it to the player's hand"""
            card = deck.draw_card()
            if card:
                self.hand.append(card)
                return card
            return None
        
        def play_card(self, index):
            """Play a card from the player's hand"""
            if 0 <= index < len(self.hand):
                return self.hand.pop(index)
            return None
    
    class MultiplayerPlayer:
        def __init__(self, name, ip, server, player2_name, opponent_id):
            # Initialize the player's name and IP address
            self.name = name
            self.ip = ip
            self.hand = []
            self.server = server  # Assign the server object
            self.server.connect(ip)  # Connect to the server using the provided IP address        
            self.player2_name = player2_name
            self.opponent_id = opponent_id
            self.player2 = playerdata(player2_name, opponent_id)  # Initialize the opponent player data

        def connection(self):
            """Establish a connection to the game server"""
            # Connection logic goes here
            pass

        def send_message(self, message):
            """Send a message to the game server"""
            # Sending message logic goes here
            pass
        
        def draw(self, deck):
            """Draw a card from the deck and add it to the player's hand"""
            card = deck.draw_card()
            if card:
                self.hand.append(card)
                return card
            return None

        def receive_message(self):
            """Receive a message from the game server"""
            # Receiving message logic goes here
            pass

        def play_card(self, index):
            """Play a card from the player's hand"""
            if 0 <= index < len(self.hand):
                return self.hand.pop(index)
            return None

        def display_hand(self):
            """Display the player's hand of cards"""
            for i, card in enumerate(self.hand):
                print(f"{i}: {card.display()}")
        
        def get_board_state(self):
            """Get the current state of the game board"""
            # Logic to get the board state goes here
            pass

        def opponent_decision(self, decision):
            """Receive the opponent's decision"""
            # Logic to handle the opponent's decision goes here
            pass
        def update_board_state(self, state):
            """Update the game board state"""
            # Logic to update the board state goes here
            pass

        def end_turn(self):
            """End the player's turn"""
            # Logic to end the turn goes here
            pass

        def check_winner(self):
            """Check if the player has won"""
            # Logic to check for a winner goes here
            pass

        def reset(self):
            """Reset the player's state for a new game"""
            self.hand = []
            # Additional reset logic goes here
            pass


        def receive_opponent_decision(self):
            """Receive the opponent's decision"""
            # Logic to receive the opponent's decision goes here
            pass

        def push_board_state_to_server(self, state):
            """Push the board state to the server"""
            # Logic to push the board state to the server goes here
            pass

    class MultiplayerOpponent:
        def __init__(self, player2_name, opponent_id, server):
            # Initialize the player's name and IP address
            self.player2_name = player2_name
            self.opponent_id = opponent_id
            self.player2 = playerdata(player2_name, opponent_id)  # Initialize the opponent player data
            self.server = server # Assign the server object the IP address of the server

        def connection(self):
            # Establish a connection to the game server. #
            try:
                # Use the ping_server function to check if the server is reachable
                from scripts.webhook import ping_server  # Import the ping_server function
                if ping_server(self.server):
                    print(f"Successfully connected to the server at {self.server}")
                    return True
                else:
                    print(f"Failed to connect to the server at {self.server}")
                    return False
            except Exception as e:
                print(f"An error occurred while connecting to the server: {e}")
                return False

        def send_message(self, message):
            """Send a message to the game server"""
            # Sending message logic goes here
            pass
        
        def draw(self, deck):
            """Draw a card from the deck and add it to the player's hand"""
            card = deck.draw_card()
            if card:
                self.hand.append(card)
                return card
            return None

        def receive_message(self):
            """Receive a message from the game server"""
            # Receiving message logic goes here
            pass

        def play_card(self, index):
            """Play a card from the player's hand"""
            if 0 <= index < len(self.hand):
                return self.hand.pop(index)
            return None

        def display_hand(self):
            """Display the player's hand of cards"""
            for i, card in enumerate(self.hand):
                print(f"{i}: {card.display()}")
        
        def get_board_state(self):
            """Get the current state of the game board"""
            # Logic to get the board state goes here
            pass

        def opponent_decision(self, decision):
            """Receive the opponent's decision"""
            # Logic to handle the opponent's decision goes here
            pass
        def update_board_state(self, state):
            """Update the game board state"""
            # Logic to update the board state goes here
            pass

        def end_turn(self):
            """End the player's turn"""
            # Logic to end the turn goes here
            pass

        def check_winner(self):
            """Check if the player has won"""
            # Logic to check for a winner goes here
            pass

        def reset(self):
            """Reset the player's state for a new game"""
            self.hand = []
            # Additional reset logic goes here
            pass


        def receive_opponent_decision(self):
            """Receive the opponent's decision"""
            # Logic to receive the opponent's decision goes here
            pass

        def push_board_state_to_server(self, state):
            """Push the board state to the server"""
            # Logic to push the board state to the server goes here
            pass

    class board:
        def __init__(self):
            # Initialize the game board with empty spaces
            self.board = [[None for _ in range(3)] for _ in range(3)]
            self.background_image = "background.png"  # Path to the background image
            self.player_colors = {
                "player1": "blue",  # Border color for Player 1
                "player2": "red"    # Border color for Player 2
            }

        def place_card(self, card, row, col, owner):
            """
            Place a card on the board at the specified position.
            If a card is placed, it interacts with adjacent cards and may take ownership.
            """
            if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] is None:
                self.board[row][col] = {"card": card, "owner": owner}
                self.check_adjacent_cards(card, row, col, owner)
                return True
            return False

        def check_adjacent_cards(self, card, row, col, owner):
            """
            Check adjacent cards and take ownership if the placed card's side value is higher.
            """
            directions = {
                "north": (-1, 0),  # Row above
                "south": (1, 0),   # Row below
                "west": (0, -1),   # Column to the left
                "east": (0, 1)     # Column to the right
            }

            for direction, (dr, dc) in directions.items():
                adj_row, adj_col = row + dr, col + dc
                if 0 <= adj_row < 3 and 0 <= adj_col < 3:
                    adjacent = self.board[adj_row][adj_col]
                    if adjacent and adjacent["card"]:
                        adjacent_card = adjacent["card"]
                        opposite_direction = {
                            "north": "south",
                            "south": "north",
                            "west": "east",
                            "east": "west"
                        }[direction]

                        if card.get_value(direction) > adjacent_card.get_value(opposite_direction):
                            # Take ownership of the adjacent card
                            self.board[adj_row][adj_col]["owner"] = owner

        def display(self):
            """
            Display the current state of the board.
            Each spot shows the card's image or "Empty" and the owner's border color.
            """
            for row in self.board:
                for spot in row:
                    if spot:
                        card = spot["card"]
                        owner = spot["owner"]
                        border_color = self.player_colors.get(owner, "white")
                        print(f"[{card.image_path} - {border_color}]")
                    else:
                        print("[Empty]")
                print("-" * 20)

        def render_board(self):
            """
            Render the board visually in the game using Ren'Py's screen language.
            """
            renpy.show_screen("game_board", board=self)

# Ren'Py screen to render the board
screen game_board(board):
    frame:
        background board.background_image
        grid 3 3 spacing 10:
            for row in board.board:
                for spot in row:
                    if spot:
                        python:
                            card = spot["card"]
                            owner = spot["owner"]
                            border_color = board.player_colors.get(owner, "white")
                        frame:
                            background card.image_path
                            style_prefix "card"
                            if owner == "player1":
                                add "blue_border.png"
                            elif owner == "player2":
                                add "red_border.png"
                    else:
                        frame:
                            background "empty_spot.png"