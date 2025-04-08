from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database config (SQLite for now, can be configured for SQL Server later)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Changed to project directory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Define the database model for Player
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    games_played = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Player {self.name}>'


# Create the database tables if they do not exist
with app.app_context():
    db.create_all()


# Routes
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Ren'Py Card Game Server is running!"}), 200


@app.route("/favicon.ico")
def favicon():
    return "", 204  # No content to avoid the 404 error for the favicon


@app.route("/join", methods=["POST"])
def join_game():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"message": "Invalid JSON"}), 400

    player_name = data.get('name')

    if not player_name:
        return jsonify({"message": "Missing player name"}), 400

    existing = Player.query.filter_by(name=player_name).first()
    if existing:
        return jsonify({"message": f"Player {player_name} already in the game!"}), 200

    new_player = Player(name=player_name)
    db.session.add(new_player)
    db.session.commit()
    return jsonify({"message": f"Player {player_name} joined the game!"}), 200


@app.route("/update_player", methods=["POST"])
def update_player():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"message": "Invalid JSON"}), 400

    player_name = data.get('name')
    player = Player.query.filter_by(name=player_name).first()

    if not player:
        return jsonify({"message": f"Player {player_name} not found!"}), 404

    # Update player stats (wins, losses, games played, score)
    player.wins = data.get('wins', player.wins)
    player.losses = data.get('losses', player.losses)
    player.score = data.get('score', player.score)  # Update score if provided
    player.games_played += 1
    db.session.commit()
    return jsonify({"message": f"Player {player_name}'s stats updated!"}), 200


@app.route("/game_state", methods=["GET"])
def game_state():
    players = Player.query.all()
    return jsonify({
        "players": [
            {"name": p.name, "wins": p.wins, "losses": p.losses, "games_played": p.games_played, "score": p.score}
            for p in players
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)
